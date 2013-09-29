#!/usr/bin/env python

from pyparsing import *
from collections import defaultdict
import re
from collections import OrderedDict

import Character
#from Character import Character, Stat, Skill, Resistance, Item, Race, Culture


###################################
### Here are the older parsing things that I currently have
###################################
def stripComments(text):
    return re.sub(r'(^|[^\\])#.*',r'\1',text)

def LoadProfessions(filename):
    """
    Loads a file, then parses the professions from it.
    Returns a dict of profession names to skill dictionary.
    The skill dictionaries are from skill name to cost list.
    """
    with open(filename) as f:
        text = f.read()
    profs = OrderedDict()
    text = stripComments(text)
    for profMatch in re.finditer(r'(\S[^{}]*?)\s*'
                                 r'((\s*\{.*?\})+)',text):
        profname = profMatch.group(1)
        skills = {}
        for skillMatch in re.finditer(r'\{(.*?)\}'
                                      ,profMatch.group(2)):
            items = [s.strip() for s in skillMatch.group(1).split(',')]
            costList = [int(s) for s in items[1:]]
            skills[items[0]] = costList
        profs[profname] = skills
    return profs

def LoadRaces(filename):
    with open(filename) as f:
        text = f.read()
    races = race.searchString(text)
    return races



##################################
### Here is the new form of parsing that I am working on
##################################
def litSup(literal):
    return Literal(literal).suppress()
def pyparsingAny(inputList):
    inputList = list(inputList)
    return reduce(lambda a,b:a^b,  inputList[1:], inputList[0])
def itemList(item,sep):
    itemSep = item.copy()
    itemSep = itemSep.addParseAction(lambda t:(sep,t[0]))
    output = (litSup(sep[0]) +
              itemSep + ZeroOrMore(litSup(',') + itemSep) +
              litSup(sep[1]))
    return output
def mergeLists(inputList):
    output = defaultdict(list)
    for key,item in inputList:
        output[key].append(item)
    return [output]
def itemOptions(*args):
    options = zip(args[0::2],args[1::2])
    fullList = pyparsingAny(itemList(item,sep) for item,sep in options)
    fullList = ungroup(ZeroOrMore(fullList))
    fullList.setParseAction(mergeLists)
    return fullList


IDCharList = alphanums + """_'"""
IDspecialDict = {'\\n':'\n','\\t':'\t'}
IDspecialRevDict = {v:k for k,v in IDspecialDict.items()}
IDspecialChar = Combine(Literal('\\') + Word(printables,exact=1)).setParseAction(
    lambda t:IDspecialDict[t[0]] if t[0] in IDspecialDict else t[0][1])
IDchar = (Word(IDCharList) ^ IDspecialChar)
ID = Combine(OneOrMore(IDchar) +
             ZeroOrMore(White(' \t') + OneOrMore(IDchar)))
number = Combine(Optional(Literal('-') ^ Literal('+'))
                 +Word(nums)).setParseAction(lambda t:int(t[0]))
IDbonus = (ID + number + Optional(Literal('r'))('ranks')
           ).setParseAction(lambda t:(t[0],t[1],'ranks' in t) )

def escape_ID(unescaped):
    return ''.join( s if s in IDCharList or s==' ' else
                    IDspecialRevDict[s] if s in IDspecialRevDict else
                    '\\'+s
                    for s in unescaped)

description = (litSup('"') + ID('desc') + litSup('"'))

def makeKeyword(m):
    return (m['keyword'],m['value'])
keywordList = ['Name','PlayerName','Profession']
_opid = Optional(ID,'')('value')
_opid.whiteChars = ' \t'
keyword = (pyparsingAny(Literal(key) for key in keywordList)('keyword')
           + litSup(':') + _opid
           ).setParseAction(makeKeyword)

keywordIntList = ['Level','Experience']
_opnum = Optional(number,0)('value')
_opnum.whiteChars = ' \t'
keywordInt = (pyparsingAny(Literal(key) for key in keywordIntList)('keyword')
              + litSup(':') + Optional(number,0)('value')
              ).setParseAction(makeKeyword)

def makeWeaponCosts(m):
    return ('WeaponCosts',[i[0] for i in m])
weaponcosts = (litSup('WeaponCosts') + litSup(':')
               + ZeroOrMore(litSup('<')
                           + delimitedList(number).setParseAction(lambda t:(list(t),))
                           + litSup('>'))
               ).setParseAction(makeWeaponCosts)

def makeWeaponOrder(m):
    return ('WeaponOrder',m)
weaponorder = (litSup('WeaponOrder') + litSup(':')
               + delimitedList(ID)).setParseAction(makeWeaponOrder)

def makeStat(m):
    return ('Stat',Character.Stat(Names=[m['name']],Value=m['value'],
                        Options=m['options']['[]'],
                        Parents=m['options']['{}'],
                        Description=m['desc'][0]))
stat = (litSup('Stat') + litSup(':')
        + ID('name')
        + itemOptions(ID,'[]')('options')
        + litSup(':') + number('value')
        + Optional(description,'')('desc')
        ).setParseAction(makeStat)

def makeSkill(m):
    output = Character.Skill(Names=[m['name']],Value=m['value'] if 'value' in m else None,
                             Options=m['options']['[]'],Parents=m['options']['{}'],
                             Costs=m['options']['<>'],
                             Description=m['desc'][0])
    return ('Skill',output)
skill = (litSup('Skill') + litSup(':')
         + ID('name')
         + itemOptions(ID,'{}',
                       ID,'[]',
                       number,'<>')('options')
         + Optional(litSup(':') + number('value'))
         + Optional(description,'')('desc')
         ).setParseAction(makeSkill)

def makeResistance(m):
    return ('Resistance',
            Character.Resistance(Names=[m['name']],
                       Parents=m['options']['{}'],
                       Description=m['desc'][0]))
resistance = (litSup('Resistance') + litSup(':')
              + ID('name')
              + itemOptions(ID,'{}')('options')
              + Optional(description,'')('desc')
              ).setParseAction(makeResistance)

def makeItem(m):
    output = Character.Item(Names=[m['name']],
                  Options=m['options']['[]'],
                  Description=m['desc'][0])
    output.SetChildValues(m['options']['{}'])
    return ('Item',output)
item = (litSup('Item') + litSup(':')
        + ID('name')
        + itemOptions(IDbonus,'{}',
                      ID,'[]')('options')
        + Optional(description,'')('desc')
        ).setParseAction(makeItem)


def makeRace(m):
    output = Character.Race(Names=[m['name']],
                  Options=m['options']['[]'],
                  Description=m['desc'][0])
    output.SetChildValues(m['options']['{}'])
    return ('Race',output)
race = (litSup('Race') + litSup(':')
        + ID('name') + itemOptions(IDbonus,'{}')('options')
        + Optional(description,'')('desc')
        ).setParseAction(makeRace)

def makeCulture(m):
    output = Character.Culture(Names=[m['name']],
                    Options=m['options']['[]'],
                     Description=m['desc'][0])
    output.SetChildValues(m['options']['{}'])
    return ('Culture',output)
culture = (litSup('Culture') + litSup(':')
           + ID('name') + itemOptions(IDbonus,'{}')('options')
           + Optional(description,'')('desc')
           ).setParseAction(makeCulture)


value = keyword | keywordInt | weaponcosts | weaponorder | stat | skill | resistance | item | race | culture

def makeCharacter(m):
    output = Character.Character()
    for tag,item in m:
        if tag in ['Name','PlayerName','Profession','Level','Experience']:
            output.SetMisc(tag,item)
        elif tag in ['Stat','Skill','Resistance','Item','Race','Culture']:
            output.AddVal(item)
        elif tag=='WeaponCosts':
            output.WeaponCostList = item
        elif tag=='WeaponOrder':
            output.WeaponOrder = item
    return output
character = OneOrMore(value).ignore(pythonStyleComment).setParseAction(makeCharacter)

if __name__=='__main__':
    import sys
    filename = sys.argv[1]
    lines = open(filename).readlines()
    text = ''.join(lines)
    c = character.parseString(text,parseAll=True)[0]
    import code; code.interact(local=locals())
