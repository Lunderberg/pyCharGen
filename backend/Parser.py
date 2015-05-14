#!/usr/bin/env python

from pyparsing import *
from collections import defaultdict
import re
from collections import OrderedDict

import Character
import CulturePrototype
import Profession

##################################
### Common things that will be used throughout
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

###################################
### Now, actually defining some syntax
###################################

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

def makeStat(m):
    return ('Stat',Character.Stat(Name=m['name'],RawValue=m['value'],
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
    value = m['value'] if 'value' in m else 0
    delta = m['delta'] if 'delta' in m else 0
    output = Character.Skill(Name=m['name'],RawValue=value,Delta=delta,
                             Options=m['options']['[]'],Parents=m['options']['{}'],
                             Costs=m['options']['<>'],
                             Description=m['desc'][0])
    return ('Skill',output)
skill = (litSup('Skill') + litSup(':')
         + ID('name')
         + itemOptions(ID,'{}',
                       ID,'[]',
                       number,'<>')('options')
         + Optional(litSup(':') + number('value') + Optional(number('delta')))
         + Optional(description,'')('desc')
         ).setParseAction(makeSkill)

def makeResistance(m):
    return ('Resistance',
            Character.Resistance(Name=m['name'],
                       Parents=m['options']['{}'],
                       Description=m['desc'][0]))
resistance = (litSup('Resistance') + litSup(':')
              + ID('name')
              + itemOptions(ID,'{}')('options')
              + Optional(description,'')('desc')
              ).setParseAction(makeResistance)

def makeItem(m):
    output = Character.Item(Name=m['name'],
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

def makeTalent(m):
    output = Character.Talent(Name=m['name'],
                  Options=m['options']['[]'],
                  Description=m['desc'][0])
    output.SetChildValues(m['options']['{}'])
    return ('Talent',output)
talent = ((litSup('Talent') | litSup('Flaw')) + litSup(':')
          + ID('name')
          + itemOptions(IDbonus,'{}',
                        ID,'[]')('options')
          + Optional(description,'')('desc')
          ).setParseAction(makeTalent)

def talentFile(filename):
    pattern = Group(OneOrMore(talent)).ignore(pythonStyleComment)
    output = pattern.parseFile(filename,parseAll=True)[0]
    return [t for tag,t in output]


def makeRace(m):
    output = Character.Race(Name=m['name'],
                  Options=m['options']['[]'],
                  Description=m['desc'][0])
    output.SetChildValues(m['options']['{}'])
    return ('Race',output)
race = (litSup('Race') + litSup(':')
        + ID('name') + itemOptions(IDbonus,'{}')('options')
        + Optional(description,'')('desc')
        ).setParseAction(makeRace)

def raceFile(filename):
    pattern = Group(OneOrMore(race)).ignore(pythonStyleComment)
    output = pattern.parseFile(filename,parseAll=True)[0]
    return [r for tag,r in output]

def makeCulture(m):
    output = Character.Culture(Name=m['name'],
                     Description=m['desc'][0])
    output.SetChildValues(m['options']['{}'])
    return ('Culture',output)
culture = (litSup('Culture') + litSup(':')
           + ID('name') + itemOptions(IDbonus,'{}')('options')
           + Optional(description,'')('desc')
           ).setParseAction(makeCulture)

def sanify(m):
    return list(m) if isinstance(m,ParseResults) else m
cultureOption_ListOption = (
    (litSup('$PREV') + Optional(number)('num')).setParseAction(
        lambda m:m['num'] if 'num' in m else 1)|
    ID |
    Literal('*').setParseAction(lambda m:0) |
    (litSup('(') + Group(delimitedList(ID,'|'))+litSup(')')) )
cultureOption = (Group(delimitedList(cultureOption_ListOption,'/'))
                 + number + Optional(Literal('r'))('ranks')
                 ).setParseAction(lambda t:(map(sanify,t[0]),t[1],'ranks' in t))
def makeCulturePrototype(m):
    return CulturePrototype.CulturePrototype(
        m['options']['{}'],Name=m['name'],Description=m['desc'][0])
culturePrototype = (litSup('CulturePrototype') + litSup(':')
                    + ID('name') + itemOptions(cultureOption,'{}')('options')
                    + Optional(description,'')('desc')
                    ).setParseAction(makeCulturePrototype)
def cultureFile(filename):
    pattern = Group(OneOrMore(culturePrototype)).ignore(pythonStyleComment)
    return pattern.parseFile(filename,parseAll=True)[0]


value = (keyword | keywordInt | weaponcosts | stat
         | skill | resistance | item | race | culture | talent)

def makeCharacter(m):
    output = Character.Character()
    for tag,item in m:
        if tag in ['Name','PlayerName','Profession','Level','Experience']:
            output.SetMisc(tag,item)
        elif tag in ['Stat','Skill','Resistance','Item','Talent']:
            output.AddVal(item)
        elif tag=='Culture':
            output.Culture = item
        elif tag=='Race':
            output.Race = item
        elif tag=='WeaponCosts':
            output.WeaponCostList = item
        elif tag=='WeaponOrder':
            output.WeaponOrder = item
    return output
character = OneOrMore(value).ignore(pythonStyleComment).setParseAction(makeCharacter)
def characterFile(filename):
    return character.parseFile(filename,parseAll=True)[0]

professionItem = (litSup('{') + ID + litSup(',')
                  + delimitedList(number)
                  + litSup('}')).setParseAction(lambda m: [(m[0],m[1:])])
def makeProfession(m):
    output = Profession.Profession(m.name)
    for skillname,cost in m.costs:
        output.AddCost(skillname,cost)
    return output
profession = (litSup('Profession') + litSup(':')
              + ID('name') + OneOrMore(professionItem)('costs')
              ).setParseAction(makeProfession)
def professionFile(filename):
    return OneOrMore(profession).parseFile(filename,parseAll=True)[:]


if __name__=='__main__':
    import sys
    filename = sys.argv[1]
    lines = open(filename).readlines()
    text = ''.join(lines)
    c = character.parseString(text,parseAll=True)[0]
    import code; code.interact(local=locals())
