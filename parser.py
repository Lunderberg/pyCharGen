#!/usr/bin/env python

from pyparsing import *
from collections import defaultdict
import re
from collections import OrderedDict

from Character import Stat, Skill, Resistance, Item, Race, Culture


###################################
### Here are the older parsing things that I currently have
###################################
def LoadProfessions(filename):
    """
    Loads a file, then parses the professions from it.
    Returns a dict of profession names to skill dictionary.
    The skill dictionaries are from skill name to cost list.
    """
    with open(filename) as f:
        text = f.read()
    profs = OrderedDict()
    #Strip out comments.
    text = re.sub(r'(^|[^\\])#.*',r'',text)
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
    return output
def itemOptions(*args):
    options = zip(args[0::2],args[1::2])
    fullList = [itemList(item,sep) for item,sep in options]
    fullList = reduce(lambda a,b:a^b,fullList[1:],fullList[0])
    fullList = ZeroOrMore(fullList)
    fullList.setParseAction(mergeLists)
    return fullList
        

nameCharList = alphanums + """_'"""
namechar = (Word(nameCharList) ^
            (litSup('\\')+Word(printables,exact=1)))
name = Combine(OneOrMore(namechar) +
               ZeroOrMore(White() + OneOrMore(namechar)))
number = Combine(Optional(Literal('-') ^ Literal('+'))
                 +Word(nums)).setParseAction(lambda t:int(t[0]))
namebonus = (name + number).setParseAction(lambda t:(t[0],t[1]) )

stat = (litSup('Stat') + litSup(':')
        + name + itemOptions(name,'[]')
        + litSup(':') + number.setResultsName('value')
        )
skill = (litSup('Skill') + litSup(':')
         + name + itemOptions(name,'{}',
                              name,'[]')
         + Optional(litSup(':') + number)
         )
resistance = (litSup('Resistance') + litSup(':')
              + name + itemOptions(name,'{}')
              )
item = (litSup('Item') + litSup(':')
        + name + itemOptions(namebonus,'{}',
                             name,'[]')
        )
race = (litSup('Race') + litSup(':')
        + name + itemOptions(namebonus,'{}')
        )

if __name__=='__main__':
    print namebonus.parseString('Swimming-10')
    print itemOptions(namebonus,'{}').parseString('{Swimming-10}')
    
    print LoadRaces('/home/eric/pyCharGen/tables/Races.txt')
