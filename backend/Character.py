#!/usr/bin/env python

import os.path as path
import re
from collections import OrderedDict
import sys

import DiceParse
from EventHandler import EventHandler
from utils import resource
import DAG
import Parser

_statBonuses = DiceParse.Table(resource('tables','StatBonus.txt'))
_skillBonuses = DiceParse.Table(resource('tables','SkillBonus.txt'))

class Character(object):
    def __init__(self):
        self.graph = DAG.DAG()
        self.MiscVals = {
            'Name':'',
            'PlayerName':'',
            'Profession':'',
            'Level':0,
            'Experience':0
            }
        self.Events = EventHandler()
    def SetMisc(self,key,val):
        if key in self.MiscVals:
            self.MiscVals[key] = val
            self.Events('Misc Changed')
        else:
            raise KeyError(val)
    def GetMisc(self,key):
        return self.MiscVals[key]
    def Update(self):
        self.Events.Execute()
    def __getitem__(self,key):
        return self.graph[key]
    def MoveTo(self,nodeA,nodeB,before=False):
        res = self.graph.MoveTo(nodeA,nodeB,before)
        if res:
            self.Events('Values Reordered',nodeA,nodeB,before)
        #Reordering the weapons changes the weapon costs.
            for val in self.Values:
                if 'Weapon' in val.Options:
                    val.Changed()
    @property
    def Values(self):
        return iter(self.graph)
    @property
    def Skills(self):
        return (val for val in self.graph if isinstance(val,Skill))
    @property
    def Stats(self):
        return (val for val in self.graph if isinstance(val,Stat))
    @property
    def Resistances(self):
        return (val for val in self.graph if isinstance(val,Resistance))
    @property
    def Items(self):
        return (val for val in self.graph if isinstance(val,Item))
    @property
    def Culture(self):
        try:
            return self._culture
        except AttributeError:
            return None
    @Culture.setter
    def Culture(self,val):
        if self.Culture is not None:
            self.RemoveVal(self.Culture)
        self._culture = val
        self.AddVal(val)
    @property
    def Race(self):
        try:
            return self._race
        except AttributeError:
            return None
    @Race.setter
    def Race(self,val):
        if self.Race is not None:
            self.RemoveVal(self.Race)
        self._race = val
        self.AddVal(val)
    def AddVal(self,newVal):
        """
        Adds the value to the list of values.
        Also, links the parent values together.
        Raises the 'Skill Added','Stat Added', or 'Resistance Added' event.
        """
        newVal.char = self
        self.graph.Add(newVal)
        self.Events('{0} Added'.format(newVal.Type),newVal)
        newVal.Events = self.Events
    def RemoveVal(self,val):
        """
        Removes the value given.
        Also, removes all children of the given value.
        Raises the 'Value Removed' event, first of the children, then of itself.
        """
        self.graph.Remove(val)
        for ch in val.Children:
            self.RemoveVal(ch)
        self.Events('{0} Removed'.format(val.Type),val)
    def ApplyLevelUp(self):
        """
        Applies the increase in level as given by the Delta of each Value.
        Increments the Level by 1.
        """
        for val in self.graph:
            val.ApplyLevelUp()
        self.SetMisc('Level',self.GetMisc('Level')+1)
    def LoadProfession(self,prof):
        """
        Expects a dictionary from skill names to a list of skill costs.
        """
        for val in self.Values:
            val.Costs = None
        self.SetMisc("Profession",prof.Name)
        weaponcosts = []
        for skill,costs in prof.Costs:
            if skill.startswith("Combat Training"):
                weaponcosts.append(costs)
            else:
                try:
                    self[skill].Costs = costs[:]
                except KeyError:
                    pass
        self.WeaponCostList = weaponcosts
    @property
    def WeaponCostList(self):
        try:
            return self._WeaponCostList
        except AttributeError:
            self._WeaponCostList = []
            return self._WeaponCostList
    @WeaponCostList.setter
    def WeaponCostList(self,val):
        """
        Set the cost of increasing each weapon skill.
        The input should be a list of lists,
          with each outer list corresponding to a weapon,
          and each inner list corresponding to the skill cost list.
        """
        self._WeaponCostList = val
        for val in self.Values:
            if 'Weapon' in val.Options:
                val.Changed()
    def WeaponCost(self,sk):
        i = -1
        weaponGen = (val for val in self.Values if 'Weapon' in val.Options)
        for weapon,cost in zip(weaponGen,self.WeaponCostList):
            if weapon is sk:
                return cost
        else:
            return []
    def StatPoints(self,levelled=False,potl=False):
        return sum(st.Points(levelled,potl) for st in self.Stats)
    def StatPointsAllowed(self,level=None,potl=False):
        if potl:
            return 355
        else:
            level = self.GetMisc('Level') if level is None else level
            return 55 if level==0 else 12
    def DPspent(self):
        return sum(sk.DPspent() for sk in self.Skills)
    def DPallowed(self):
        return 50
    def SaveString(self):
        lines = ['{0}: {1}'.format(Parser.escape_ID(k),v) for k,v in self.MiscVals.items()]
        lines += ['WeaponCosts: ' + ' '.join('<' + ','.join(str(i) for i in ilist) + '>'
                                             for ilist in self.WeaponCostList)]
        #Escape all the character-based lines.
        #The Value-based lines are escaped in Value.SaveString()
        lines += [val.SaveString() for val in self.graph]
        return '\n'.join(lines)
    @staticmethod
    def Open(filename):
        """Given a filename, constructs and returns the character as read from the file"""
        return Parser.characterFile(filename)


class Value(object):
    """
    Base class for Stats, Skills, Resistances, Items, etc.
    Can have an EventHandler to give notification when the value is changed.
    Subclasses change eventKey to change the key passed to the EventHandler
    """
    Type = 'Value'
    _escape_chars = [('\n',r'\n'),
                     ('"','\\"'),]
    def __init__(self,Value=None,Name='',Parents=None,Children=None,Options=None,Description=""):
        self.Events = lambda *args:None
        self.graph = None
        self.Name = Name
        self.requestedParents = [] if Parents is None else Parents
        self.requestedChildren = [] if Children is None else Children
        self.Options = [] if Options is None else Options
        self._value = None
        self.Value = Value
        self.Description = Description
        self.Delta = 0
    def __repr__(self):
        return '{0}(Value={4}, Name="{1}", Options={2}, Parents={3}, Description="{5}")'.format(
            self.Type,self.Name,self.Options,self.requestedParents,self.Value,self.Description)
    @property
    def Name(self):
        return self._Name
    @Name.setter
    def Name(self,val):
        self._Name = val
        self.Changed(False)
    @property
    def Parents(self):
        if self.graph is not None:
            return self.graph.Parents(self)
        else:
            return []
    @property
    def Children(self):
        if self.graph is not None:
            return self.graph.Children(self)
        else:
            return []
    @property
    def Value(self):
        return 0 if self._value is None else self._value
    @Value.setter
    def Value(self,val):
        if self.IsValid(val):
            self._value = val
            self.Changed()
    @property
    def _valueAndExtra(self):
        return self.Value + sum(par.ExtraValue(self) for par in self.Parents)
    def IsValid(self,val):
        return True
    @property
    def Delta(self):
        return self._delta
    @Delta.setter
    def Delta(self,val):
        self._delta = val
        self.Changed()
    @property
    def Description(self):
        return self._Description
    @Description.setter
    def Description(self,val):
        self._Description = val
        self.Changed(False)
    @property
    def NoBonus(self):
        return 'NoBonus' in self.Options
    @NoBonus.setter
    def NoBonus(self,val):
        if val and not self.NoBonus:
            self.Options.append('NoBonus')
        elif not val and self.NoBonus:
            self.Options.remove('CommonlyUsed')
        self.Changed()
    def Changed(self,propagate=True):
        self.Events('Value Changed',self)
        self.Events(self.Type+' Changed',self)
        if propagate:
            for ch in self.Children:
                ch.Changed()
    def ApplyLevelUp(self):
        if self.Value is not None:
            self.Value += self.Delta
            self.Delta = 0
    def ValueBonus(self,asker=None,levelled=False):
        return 0
    def ExtraValue(self,asker=None,levelled=False):
        return 0
    def Bonus(self,asker=None,levelled=False,verbose=False):
        return self.ValueBonus(asker,levelled) + sum(par.Bonus(self,levelled) for par in self.Parents)
    def CategoryBonus(self,asker=None,levelled=False):
        return sum(par.Bonus(self,levelled) for par in self.Parents if isinstance(par,Skill) and not par.NoBonus)
    def StatBonus(self,asker=None,levelled=False):
        return (sum(par.Bonus(self,levelled) for par in self.Parents if isinstance(par,Stat))
               + sum(par.StatBonus(self,levelled) for par in self.Parents if par.NoBonus))
    def ItemBonus(self,asker=None,levelled=False):
        return (sum(par.Bonus(self,levelled) for par in self.Parents if isinstance(par,Item))
                +sum(par.Bonus(self,levelled) for par in self.Parents if par.NoBonus))
    def RelativeSaveString(self):
        return ', '.join(Parser.escape_ID(par.Name) for par in self.graph.OwnedParents(self))
    def CostSaveString(self):
        return ''
    def SaveString(self):
        relatives = self.RelativeSaveString()
        relatives = '{' + relatives + '}' if relatives else ''
        costs = self.CostSaveString()
        costs = '<' + costs + '>' if costs else ''
        opts = ('[' + ', '.join(self.Options) + ']'
                if self.Options else '')
        val = (': ' + str(self.Value)
               if self.Value!=0 else '')
        descript = Parser.escape_ID(self.Description) if self.Description else ''
        descript = ('"' + descript + '"') if descript else ''
        out = ' '.join(s for s in [Parser.escape_ID(self.Name),relatives,opts,costs,val,descript] if s)
        return '{0}: {1}'.format(self.Type,out)
    @staticmethod
    def FromLine(line):
        return Parser.value.parseString(line)[0][1]

class Stat(Value):
    Type = 'Stat'
    @property
    def Min(self):
        for opt in self.Options:
            if opt[:3]=='Min':
                try:
                    return int(opt[3:])
                except:
                    pass
        else:
            return 1
    @Min.setter
    def Min(self,val):
        self.Options = [opt for opt in self.Options if opt[:3]!='Min']
        self.Options.append('Min' + '{0:+d}'.format(val))
        self.Changed(False)
    @property
    def Max(self):
        for opt in self.Options:
            if opt[:3]=='Max':
                try:
                    return int(opt[3:])
                except:
                    pass
        else:
            return 50
    @Max.setter
    def Max(self,val):
        self.Options = [opt for opt in self.Options if opt[:3]!='Max']
        self.Options.append('Max' + '{0:+d}'.format(val))
        self.Changed(False)
    def IsValid(self,val):
        return 1 <= val <= 100
    def ValueBonus(self,asker=None,levelled=False,potl=False):
        if self.NoBonus:
            return 0
        elif potl:
            return _statBonuses(self.Max)
        else:
            return _statBonuses(self._valueAndExtra + (self.Delta if levelled else 0))
    def Points(self,levelled=False,potl=False):
        if self.NoBonus:
            return 0
        elif potl:
            return _statBonuses(self.Max,item=1)
        else:
            return _statBonuses(self._valueAndExtra + (self.Delta if levelled else 0),item=1)

class Resistance(Value):
    Type = 'Resistance'

class Skill(Value):
    Type = 'Skill'
    def __init__(self,Costs=None,*args,**kwargs):
        super(Skill,self).__init__(*args,**kwargs)
        self.Costs = None if Costs is None else Costs
    def __repr__(self):
        return '{0}(Value={4}, Name="{1}", Options={2}, Parents={3}, Costs={5},Description="{6}")'.format(
            self.Type,self.Name,self.Options,self.requestedParents,self.Value,self.Costs,self.Description)
    def ValueBonus(self,asker=None,levelled=False):
        return 0 if self.NoBonus else _skillBonuses(self._valueAndExtra + (self.Delta if levelled else 0))
    @property
    def CommonlyUsed(self):
        return 'CommonlyUsed' in self.Options
    @CommonlyUsed.setter
    def CommonlyUsed(self,val):
        current = 'CommonlyUsed' in self.Options
        if val and not current:
            self.Options.append('CommonlyUsed')
        elif not val and current:
            self.Options.remove('CommonlyUsed')
        self.Changed(False)
    @property
    def Costs(self):
        """
        Return a list of integers given the cost of levelling up skills.
        If the skill is tagged as 'Weapon', queries the character to find what weapon cost there is.
        If the current skill has no cost, looks in parent skills.
        """
        if self._costs:
            return self._costs
        elif 'Weapon' in self.Options and self.char is not None:
            return self.char.WeaponCost(self)
        for par in self.Parents:
            if isinstance(par,Skill):
                res = par.Costs
                if res:
                    return par.Costs
        return []
    @Costs.setter
    def Costs(self,val):
        self._costs = val
        self.Changed()
    def CostSaveString(self):
        return '' if self._costs is None else ','.join(str(i) for i in self._costs)
    @property
    def Depth(self):
        parSkills = [val for val in self.Parents if isinstance(val,Skill)]
        if parSkills:
            return parSkills[0].Depth+1
        else:
            return 0
    def DPspent(self):
        return sum(self.Costs[:self.Delta])

class MultiValue(Value):
    Type = 'MultiValue'
    BonusOps = '+-'
    def __init__(self,*args,**kwargs):
        super(MultiValue,self).__init__(*args,**kwargs)
        self.MakeList(self.requestedChildren)
    def __repr__(self):
        return '{0}(Name="{1}", Options={2}, ChildValues={3})'.format(
            self.Type,self.Name,self.Options,self.ChildValues)
    def ChangeBonuses(self,bonusStr):
        newList = [s.strip() for s in bonusStr.split(',')]
        oldChList = self.ChildValues
        self.MakeList(newList)
        newChList = self.ChildValues
        if self.graph is not None:
            self.graph.Remove(self)
            self.graph.Add(self)
        if newChList != oldChList:
            self.Changed()
    def MakeList(self,chList):
        """
        Constructs the list of requestedChildren and ChildValues.
        Expects input as an iterable of strings, each in the form 'NameBonus'.
                   e.g. "Axe+3", "Religious Lore-5"
        """
        childvalues = []
        for ch in chList:
            if sum(ch.count(c) for c in self.BonusOps)!=1:
                continue
            index = max(ch.find(c) for c in self.BonusOps)
            name,value = ch[:index].strip(),ch[index:].strip()
            ranks = (value[-1]=='r')
            if ranks:
                value = value[:-1]
            try:
                value = int(value)
            except ValueError:
                continue
            childvalues.append((name,value,ranks))
        self.SetChildValues(childvalues)
    def SetChildValues(self,childvalues):
        self.ChildValues = childvalues
        self.requestedChildren = [name for name,bonus,ranks in childvalues]
    def RelativeSaveString(self):
        if self.ChildValues:
            return ', '.join(Parser.escape_ID(name if isinstance(name,str) else name.Name)
                             +'{0:+d}'.format(val)
                             +('r' if ranks else '')
                             for name,val,ranks in self.ChildValues)
        else:
            return ''
    def ExtraValue(self,asker=None,levelled=False):
        if asker is None or self.NoBonus:
            return 0
        for name,bonus,ranks in self.ChildValues:
            if ((name==asker.Name) or (name is asker)) and ranks:
                return bonus
        else:
            return 0
    def ValueBonus(self,asker=None,levelled=False):
        if asker is None or self.NoBonus:
            return 0
        for name,bonus,ranks in self.ChildValues:
            if ((name==asker.Name) or (name is asker)) and not ranks:
                return bonus
        else:
            return 0

class Item(MultiValue):
    Type = 'Item'

class Race(MultiValue):
    Type = 'Race'

class Culture(MultiValue):
    Type = 'Culture'
