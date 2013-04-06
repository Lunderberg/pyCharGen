#!/usr/bin/env python

import re
from collections import OrderedDict

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

        
if __name__=='__main__':
    import pprint
    LoadProfessions('tables/Professions.txt')

