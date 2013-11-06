#!/usr/bin/env python

from collections import defaultdict
import Character

# options should be list of (list,int,bool) tuples
# Each element of the list should be either a string, a list of strings, a 0 for wildcard,
#   or n >= 1 for the skill specified n options earlier.
# An option of n >= 1 is only valid as the first option.
# The integer is the bonus to be given.
# The bool, if true, has a bonus number of ranks applied instead of a flat bonus.

class CulturePrototype(object):
    def __init__(self,options,char=None,Name='',Description=''):
        self.options = options
        self.char = char
        self.Name = Name
        self.Description = Description
    @property
    def char(self):
        try:
            return self._char
        except AttributeError:
            return None
    @char.setter
    def char(self,val):
        self._char = val
        if val is not None:
            self._load_char()
    def __len__(self):
        return len(self.options)
    def _load_char(self):
        self.choices = defaultdict(lambda :None)
        self._option_list = defaultdict(list)
        self.depends = defaultdict(list)
        self.depth = defaultdict(int)
        for i,option in enumerate(self.options):
            self._make_option_list(i)
            firstcond = option[0][0]
            if isinstance(firstcond,int) and firstcond>0:
                self.depends[i-firstcond].append(i)
                self.depth[i] = self.depth[i-firstcond]+1
    def _make_option_list(self,optI):
        self._option_list[optI] = [val for val in self.char.Values if self._ismatch(optI,val)]
        if optI in self.choices:
            del self.choices[optI]
    def _ismatch(self,optI,val,all_conds = None):
        if all_conds is None:
            all_conds = self.options[optI][0]
        cond = all_conds[-1]
        cond_matches = ((cond==0) or
                        (isinstance(cond,str) and cond==val.Name) or
                        (isinstance(cond,list) and any(c==val.Name for c in cond)) or
                        (isinstance(cond,int) and (val is self.Choice(optI-cond))))
        if len(all_conds)==1:
            return cond_matches
        else:
            return cond_matches and any(self._ismatch(optI,par,all_conds[:-1])
                                        for par in val.Parents)
    def Depth(self,optI):
        return self.depth[optI]
    def Options(self,optI):
        return self._option_list[optI]
    def Bonus(self,optI):
        return (self.options[optI][1],self.options[optI][2])
    def Choice(self,optI):
        if optI in self.choices:
            return self.choices[optI]
        elif len(self.Options(optI))==1:
            return self.Options(optI)[0]
        else:
            return None
    def Select(self,optI,choiceI):
        self.choices[optI] = self._option_list[optI][choiceI]
        for dep in self.depends[optI]:
            self._make_option_list(dep)
        return self.depends[optI]
    @property
    def Culture(self):
        output = Character.Culture(Name=self.Name,
                                   Description=self.Description)
        childvalues = [(self.Choice(i),self.options[i][1],self.options[i][2])
                       for i in range(len(self.options)) if self.Choice(i) is not None]
        output.SetChildValues(childvalues)
        return output
