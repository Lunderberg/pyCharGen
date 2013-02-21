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
    def SetMisc(self,key,val):
        if key in self.MiscVals:
            self.MiscVals[key] = val
            self.Events('Misc Changed')
        else:
            raise KeyError(val)
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
    @property
    def Items(self):
        return (val for val in self.LinkedVals if isinstance(val,Item))
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
                self._lookup[reqCh].Changed()
        for n in val.Names:
            self._lookup[n] = val
    def UnlinkVal(self,val):
        """
        Removes all instances of a value from self.Links.
        Possible future modification: Removing only links caused by one's own requests.
        """
        toRemove = []
        for i,(par,ch) in enumerate(self.Links):
            if (par is val) or (ch is val):
                toRemove.append(i)
        for i in reversed(toRemove):
            del self.Links[i]
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
            #Removes all comments, skips if line is empty.
            res = re.search(r'(^|[^\\])#',line) #Finds a pound sign not preceded by a slash.
            if res:
                line = line[:res.end()-1]
            line.replace(r'\#','#')
            line = line.strip()
            if not line:
                continue

            nameChars = r"[\w ,-/]"
            res = re.match(r"\s*(?P<name>" +nameChars+ "+?)" #The key
                           r"\s*:\s*" #The divider
                           r"(?P<val>" +nameChars+ "+)" #The value
                           r"\s*\Z", #End of line
                           line)
            if res:
                name,val = res.group('name','val')
                if name in ['Name','PlayerName','Profession','Race','Culture']:
                    c.SetMisc(name,val)
                elif name in ['Level','Experience']:
                    try:
                        c.SetMisc(name,int(val))
                    except ValueError:
                        pass
                continue

            c.AddVal(Value.FromLine(line))
        return c

class Value(object):
    """
    Base class for Stats and Skills
    Can have an EventHandler to give notification when the value is changed.
    Subclasses change eventKey to change the key passed to the EventHandler
    """
    Type = 'Value'
    _escape_chars = [('\n',r'\n'),
                     ('"','\\"'),]
    def __init__(self,Value=None,Names=None,Parents=None,Children=None,Options=None,Description=""):
        self.Events = lambda *args:None
        self.char = None
        self.Names = [] if Names is None else Names
        self.requestedParents = [] if Parents is None else Parents
        self.requestedChildren = [] if Children is None else Children
        self.Options = [] if Options is None else Options
        self.Value = Value
        self.Description = Description
    @property
    def Name(self):
        return self.Names[0]
    @Name.setter
    def Name(self,val):
        self.Names[0] = val
        self.Changed()
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
    @property
    def Description(self):
        return self._Description
    @Description.setter
    def Description(self,val):
        self._Description = val
        self.Changed()
    def Changed(self):
        self.Events(self.Type+' Changed',self)
        for ch in self.Children:
            ch.Changed()
    def SelfBonus(self,asker=None):
        return 0
    def Bonus(self,asker=None):
        return self.SelfBonus(asker) + sum(par.Bonus(self) for par in self.Parents)
    def RelativeSaveString(self):
        parnames = [par.ShortestName for par in self.Parents]
        pars = ', '.join(parnames) if parnames else ''
        return pars
    def SaveString(self):
        nicks = ('(' + ', '.join(self.Names[1:]) + ')'
                 if len(self.Names)>1 else '')
        relatives = self.RelativeSaveString()
        relatives = '{' + relatives + '}' if relatives else ''
        opts = ('[' + ', '.join(self.Options) + ']'
                if self.Options else '')
        val = (': ' + str(self._value)
               if self._value is not None else '')
        descript = ('"' + self.Description + '"') if self.Description else ''
        out = ' '.join(s for s in [self.Name,nicks,relatives,opts,val,descript] if s)
        for unescaped,escaped in self._escape_chars:
            out = out.replace(unescaped,escaped)
        return out
    @classmethod
    def FromLine(cls,line):
        elements = [t for t in
                    [s.strip() for s in re.split(r'([(){}[\]<>:"])',line)]
                    if t]
        names = []
        relatives = []
        opts = []
        costs = []
        value = None
        description = ""

        current_type = 'main_name'
        type_dict = {'[':'opt',']':'main_name','{':'relative','}':'main_name',
                     '(':'nicknames',')':'main_name','<':'costs','>':'main_name',
                     ':':'value','"':'quote'}
                     
        for ele in elements:
            if current_type=='quote':
                if ele=='"' and description[-1]!='\\':
                    current_type='main_name'
                else:
                    description += ele
            elif ele in type_dict:
                current_type = type_dict[ele]
            elif current_type=='main_name':
                names.append(ele)
            elif current_type=='opt':
                opts.extend(s.strip() for s in ele.split(','))
            elif current_type=='relative':
                relatives.extend(s.strip() for s in ele.split(','))
            elif current_type=='nicknames':
                names.extend(s.strip() for s in ele.split(','))
            elif current_type=='costs':
                try:
                    costs.extend(int(s.strip()) for s in ele.split(','))
                except ValueError:
                    pass
            elif current_type=='value':
                try:
                    value = int(ele.strip())
                except ValueError:
                    pass

        for unescaped,escaped in cls._escape_chars:
            description = description.replace(escaped,unescaped)

        if 'Skill' in opts:
            return Skill(Value=value,Names=names,Parents=relatives,Options=opts,Description=description)
        elif 'Stat' in opts:
            return Stat(Value=value,Names=names,Parents=relatives,Options=opts,Description=description)
        elif 'Resistance' in opts:
            return Resistance(Value=value,Names=names,Parents=relatives,Options=opts,Description=description)
        elif 'Item' in opts:
            return Item(Value=value,Names=names,Children=relatives,Options=opts,Description=description)
        else:
            return Value(Value=value,Names=names,Parents=relatives,Options=opts,Description=description)


class Stat(Value):
    Type = 'Stat'
    def SelfBonus(self,asker=None):
        return 0 if 'NoBonus' in self.Options else _statBonuses(self.Value)

class Resistance(Value):
    Type = 'Resistance'

class Skill(Value):
    Type = 'Skill'
    def SelfBonus(self,asker=None):
        return 0 if 'NoBonus' in self.Options else _skillBonuses(self.Value)

class Item(Value):
    Type = 'Item'
    BonusOps = '+-'
    def __init__(self,*args,**kwargs):
        super(Item,self).__init__(*args,**kwargs)
        self.MakeList(self.requestedChildren)
    def ChangeBonuses(self,bonusStr):
        newList = [s.strip() for s in bonusStr.split(',')]
        self.MakeList(newList)
        if self.char is not None:
            self.char.UnlinkVal(self)
            self.char.LinkVal(self)
        self.Changed()
    def MakeList(self,chList):
        """
        Constructs the list of requestedChildren and ChildValues.
        Expects input as an iterable of strings, each in the form 'NameBonus'.
                   e.g. "Axe+3", "Religious Lore-5"
        """
        self.requestedChildren = []
        self.ChildValues = []
        for ch in chList:
            if sum(ch.count(c) for c in self.BonusOps)!=1:
                continue
            index = max(ch.find(c) for c in self.BonusOps)
            name,value = ch[:index].strip(),ch[index:].strip()
            try:
                value = int(value)
            except ValueError:
                continue
            self.requestedChildren.append(name)
            self.ChildValues.append((name,value))
    def RelativeSaveString(self):
        if self.ChildValues:
            return ', '.join('{0}{1:+d}'.format(name,val) for name,val in self.ChildValues)
        else:
            return ''
    def SelfBonus(self,asker=None):
        if asker is None:
            return 0
        for name,bonus in self.ChildValues:
            if name in asker.Names:
                return bonus
        else:
            return 0
