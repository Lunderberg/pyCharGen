#!/usr/bin/env python

import os.path as path
import re
from collections import OrderedDict

import DiceParse
from EventHandler import EventHandler

location = path.dirname(__file__)
_statBonuses = DiceParse.Table(path.join(location,'tables','StatBonus.txt'))
_skillBonuses = DiceParse.Table(path.join(location,'tables','SkillBonus.txt'))

class Character(object):
    def __init__(self):
        self.LinkedVals = []
        self.Links = []
        self._lookup = {}
        self.MiscVals = {
            'Name':'',
            'PlayerName':'',
            'Profession':'',
            'Race':'',
            'Culture':'',
            'Level':0,
            'Experience':0
            }
        self.Events = EventHandler()
    def __getitem__(self,key):
        return self._lookup[key]
    def __getattr__(self,key):
        try:
            return self.MiscVals[key]
        except KeyError:
            raise AttributeError(key)
    @property
    def Skills(self):
        return (val for val in self.LinkedVals if isinstance(val,Skill))
    @property
    def Stats(self):
        return (val for val in self.LinkedVals if isinstance(val,Stat))
    @property
    def Resistances(self):
        return (val for val in self.LinkedVals if isinstance(val,Resistance))
    def AddVal(self,newVal):
        """
        Adds the value to the list of values.
        Also, links the parent values together.
        Raises the 'Skill Added','Stat Added', or 'Resistance Added' event.
        """
        newVal.char = self
        self.LinkVal(newVal)
        self.LinkedVals.append(newVal)

        self.Events('{0} Added'.format(newVal.Type),newVal)
        newVal.Events = self.Events
    def RelinkAllVals(self):
        """
        Clears, then remakes all parent-child links based on the
        requested link from each Value.
        """
        self._lookup.clear()
        self.Links.clear()
        for val in self.LinkedVals:
            self.LinkVal(val)
    def LinkVal(self,val):
        """
        Looks up the requested parents and requested children.
        If found, adds them to the list of Links as (parent,child) tuples.
        """
        for reqPar in val.requestedParents:
            if reqPar in self._lookup:
                self.Links.append( (self._lookup[reqPar],val) )
        for reqCh in val.requestedChildren:
            if reqCh in self._lookup:
                self.Links.append( (val,self._lookup[reqCh]) )
        for n in val.Names:
            self._lookup[n] = val
    def RemoveVal(self,val):
        """
        Removes the value given.
        Also, removes all children of the given value.
        Raises the 'Value Removed' event, first of the children, then of itself.
        """
        self.LinkedVals.remove(val)
        for ch in val.Children:
            self.RemoveVal(ch)
        self.Events('{0} Removed'.format(val.Type),val)
    def SaveString(self):
        lines = ['{0}: {1}'.format(k,v) for k,v in self.MiscVals.items()]
        lines += [val.SaveString() for val in self.LinkedVals]
        return '\n'.join(lines)
    @staticmethod
    def Open(filename):    
        """Given a filename, constructs and returns the character as read from the file"""
        with open(filename) as f:
            lines = [line.strip() for line in f]
        c = Character()
        for line in lines:
            nameChars = r"[\w ,-/]"
            res = re.match(r"\s*(?P<name>" +nameChars+ "+?)" #The key
                           r"\s*:\s*" #The divider
                           r"(?P<val>" +nameChars+ "+)" #The value
                           r"\s*\Z", #End of line
                           line)
            if res:
                name,val = res.group('name','val')
                if name in ['Name','PlayerName','Profession','Race','Culture']:
                    c.MiscVals[name] = val
                elif name in ['Level','Experience']:
                    try:
                        c.MiscVals[name] = int(val)
                    except ValueError:
                        pass

            res = re.match(r"\s*(?P<name>" +nameChars+ r"+?)\s*" #The name
                           r"(\((?P<nicknames>" +nameChars+ r"+)\))?\s*" #Alternate names
                           r"(\{(?P<pars>" +nameChars+ r"+)\})?\s*" #The list of parents
                           r"(\[(?P<opts>" +nameChars+ r"+)\])?\s*" #The list of options
                           r"(:\s*(?P<val>\d+))?\s*" #The value itself
                           r"\Z", #At the end of the line
                           line)
            if res:
                name,nicks,parents,options,value = res.group('name','nicknames','pars','opts','val')
                nicks = [] if nicks is None else [s.strip() for s in nicks.split(',')]
                names = [name]+nicks
                parents = [] if parents is None else [s.strip() for s in parents.split(',')]
                options =  [] if options is None else [s.strip() for s in options.split(',')]
                value = None if value is None else int(value)
                
                if value is None and 'NoBonus' not in options:
                    pass
                elif 'Stat' in options:
                    c.AddVal(Stat(value,Names=names,Parents=parents,Options=options))
                elif 'Skill' in options:
                    c.AddVal(Skill(value,Names=names,Parents=parents,Options=options))
                elif 'Resistance' in options:
                    c.AddVal(Resistance(value,Names=names,Parents=parents,Options=options))
        return c

class Value(object):
    """
    Base class for Stats and Skills
    Can have an EventHandler to give notification when the value is changed.
    Subclasses change eventKey to change the key passed to the EventHandler
    """
    Type = 'Value'
    def __init__(self,Value,Names=None,Parents=None,Children=None,Options=None):
        self.Events = lambda *args:None
        self.char = None
        self.Names = [] if Names is None else Names
        self.requestedParents = [] if Parents is None else Parents
        self.requestedChildren = [] if Children is None else Children
        self.Options = [] if Options is None else Options
        self.Value = Value
    @property
    def Name(self):
        return self.Names[0]
    @property
    def ShortestName(self):
        return min(self.Names,key=len)
    @property
    def Parents(self):
        if self.char is not None:
            for par,ch in self.char.Links:
                if self is ch:
                    yield par
    @property
    def Children(self):
        if self.char is not None:
            for par,ch in self.char.Links:
                if self is par:
                    yield ch
    @property
    def Value(self):
        return 0 if self._value is None else self._value
    @Value.setter
    def Value(self,val):
        self._value = val
        self.Changed()
    def Changed(self):
        self.Events(self.Type+' Changed',self)
        for ch in self.Children:
            ch.Changed()
    @property
    def SelfBonus(self):
        return 0
    @property
    def Bonus(self):
        return self.SelfBonus + sum(par.Bonus for par in self.Parents
                                    if not isinstance(par,str))
    def SaveString(self):
        nicks = (' (' + ', '.join(self.Names[1:]) + ')'
                 if len(self.Names)>1 else '')
        parnames = [par.ShortestName for par in self.Parents]
        pars = (' {' + ', '.join(parnames) + '}'
                if parnames else '')
        opts = (' [' + ', '.join(self.Options) + ']'
                if self.Options else '')
        val = (': ' + str(self._value)
               if self._value is not None else '')
        return self.Name + nicks + pars + opts + val

class Stat(Value):
    Type = 'Stat'
    @property
    def SelfBonus(self):
        return 0 if 'NoBonus' in self.Options else _statBonuses(self.Value)

class Resistance(Value):
    Type = 'Resistance'

class Skill(Value):
    Type = 'Skill'
    @property
    def SelfBonus(self):
        return 0 if 'NoBonus' in self.Options else _skillBonuses(self.Value)
