#!/usr/bin/env python

from pyparsing import *
from collections import defaultdict
import re
from collections import OrderedDict

from Character import Stat, Skill, Resistance, Item, Race, Culture


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
    fullList = [itemList(item,sep) for item,sep in options]
    fullList = reduce(lambda a,b:a^b,fullList[1:],fullList[0])
    fullList = ungroup(ZeroOrMore(fullList))
    fullList.setParseAction(mergeLists)
    return fullList
        

IDCharList = alphanums + """_'"""
IDchar = (Word(IDCharList) ^
            (litSup('\\')+Word(printables,exact=1)))
ID = Combine(OneOrMore(IDchar) +
             ZeroOrMore(White() + OneOrMore(IDchar)))
number = Combine(Optional(Literal('-') ^ Literal('+'))
                 +Word(nums)).setParseAction(lambda t:int(t[0]))
IDbonus = (ID + number).setParseAction(lambda t:(t[0],t[1]) )

def makeStat(m):
    return Stat(Names=[m['name']],Value=m['value'],
                Options=m['options']['[]'],Parents=m['options']['{}'])
stat = (litSup('Stat') + litSup(':')
        + ID('name')
        + itemOptions(ID,'[]')('options')
        + litSup(':') + number('value')
        ).setParseAction(makeStat)

def makeSkill(m):
    return Skill(Names=[m['name']],Value=m['value'] if 'value' in m else None,
                 Options=m['options']['[]'],Parents=m['options']['{}'],Costs=m['options']['<>'])
skill = (litSup('Skill') + litSup(':')
         + ID('name')
         + itemOptions(ID,'{}',
                       ID,'[]',
                       number,'<>')('options')
         + Optional(litSup(':') + number('value'))
         ).setParseAction(makeSkill)

def makeResistance(m):
    return Resistance(Names=[m['name']],
                      Parents=m['options']['{}'])
resistance = (litSup('Resistance') + litSup(':')
              + ID('name')
              + itemOptions(ID,'{}')('options')
              ).setParseAction(makeResistance)

def makeItem(m):
    return Item(Names=[m['name']],
                Children=['{0}{1:+d}'.format(i,j) for i,j in m['options']['{}']],
                Options=m['options']['[]'])
item = (litSup('Item') + litSup(':')
        + ID('name')
        + itemOptions(IDbonus,'{}',
                      ID,'[]')('options')
        ).setParseAction(makeItem)


def makeRace(m):
    return Race(Names=[m['name']],
                Children=['{0}{1:+d}'.format(i,j) for i,j in m['options']['{}']],
                Options=m['options']['[]'])
race = (litSup('Race') + litSup(':')
        + ID('name') + itemOptions(IDbonus,'{}')('options')
        ).setParseAction(makeRace)

def makeCulture(m):
    return Culture(Names=[m['name']],
                   Children=['{0}{1:+d}'.format(i,j) for i,j in m['options']['{}']],
                   Options=m['options']['[]'])
culture = (litSup('Culture') + litSup(':')
           + ID('name') + itemOptions(IDbonus,'{}')('options')
           ).setParseAction(makeCulture)
    

value = stat | skill | resistance | item | race | culture

if __name__=='__main__':
    lines = open('TestChar_newFormat.txt').readlines()
    for linenum in [24,35,43,50]:
        try:
            print value.parseString(lines[linenum])[0]
        except ParseException:
            print "Couldn't parse",lines[linenum][:-1]
