#!/usr/bin/env python

import gtk
import gobject

class StatStore(gtk.ListStore,object):
    store_format = [
        ('Stat',gobject.TYPE_PYOBJECT),
        ('Name',str),('Temporary',int),('SelfBonus',int),('Bonus',int)
        ]
    names = {n:i for i,(n,t) in enumerate(store_format)}
    types = [t for n,t in store_format]
    def __init__(self,char):
        gtk.ListStore.__init__(self,*self.types)
        self.UpdateAll(char)
    @classmethod
    def col(cls,key):
        return cls.names[key]
    @property
    def IterAll(self):
        loc = self.get_iter_first()
        while loc:
            yield loc
            loc = self.iter_next(loc)
    def UpdateAll(self,char):
        self.clear()
        for st in char.Stats:
            stIter = self.append()
            self.set(stIter,self.col('Stat'),st)
            self.UpdateStat(stIter)
    def UpdateStat(self,stIter):
        st = self.get(stIter,self.col('Stat'))[0]
        self.set(stIter,
                 self.col('Name'),st.Name,
                 self.col('Temporary'),st.Value,
                 self.col('SelfBonus'),st.SelfBonus,
                 self.col('Bonus'),st.Bonus)
    def OnStatChange(self,stat):
        for stIter in self.IterAll:
            if stat is self.get(stIter,self.col('Stat'))[0]:
                self.UpdateStat(stIter)

class SkillStore(gtk.TreeStore,object):
    store_format = [
        ('Skill',gobject.TYPE_PYOBJECT),
        ('Name',str),('Ranks',int),('SelfBonus',int),('Bonus',int),
        ('Parents',str)
        ]
    names = {n:i for i,(n,t) in enumerate(store_format)}
    types = [t for n,t in store_format]
    def __init__(self,char):
        gtk.TreeStore.__init__(self,*self.types)
        self.UpdateAll(char)
    @classmethod
    def col(cls,key):
        return cls.names[key]
    @property
    def IterAll(self):
        path = []
        first = self.get_iter_first()
        if first is not None:
            path.append(first)
        while path:
            loc = path.pop()
            child = self.iter_children(loc)
            afterLoc = self.iter_next(loc)
            yield loc
            if afterLoc is not None:
                path.append(afterLoc)
            if child is not None:
                path.append(child)
    def UpdateAll(self,char):
        self.clear()
        usedIters = {}
        for sk in char.Skills:
            parIter = None
            for par in sk.Parents:
                if (not isinstance(par,str) and 
                    par.Name in usedIters):
                    parIter = usedIters[par.Name]
                    break
            chIter = self.append(parIter)
            usedIters[sk.Name] = chIter
            self.set(chIter,self.col('Skill'),sk)
            self.UpdateSkill(chIter)
    def UpdateSkill(self,skIter):
        sk = self.get(skIter,self.col('Skill'))[0]
        self.set(skIter,
                 self.col('Name'),sk.Name,
                 self.col('Ranks'),sk.Value,
                 self.col('SelfBonus'),sk.SelfBonus,
                 self.col('Bonus'),sk.Bonus)
    def OnSkillAdd(self,skill):
        pars = list(skill.Parents)
        for skIter in self.IterAll:
            if self.get(skIter,self.col('Skill'))[0] in pars:
                parIter = skIter
                break
        else:
            parIter = None
        chIter = self.append(parIter)
        self.set(chIter,self.col('Skill'),skill)
        self.UpdateSkill(chIter)
    def OnSkillChange(self,skill):
        for skIter in self.IterAll:
            if skill is self.get(skIter,self.col('Skill'))[0]:
                self.UpdateSkill(skIter)
    def OnSkillRemove(self,skill):
        for skIter in self.IterAll:
            if skill is self.get(skIter,self.col('Skill'))[0]:
                self.remove(skIter)
                return

def AddTextColumn(treeview,name,columnnumber,sortable=False,editable=None,xalign=0.0):
    CellText = gtk.CellRendererText()
    output = gtk.TreeViewColumn(name)
    output.pack_start(CellText,True)
    output.add_attribute(CellText,'text',columnnumber)
    if editable:
        CellText.set_property('editable',True)
        CellText.connect('edited',editable,columnnumber)
    if sortable:
        output.set_sort_column_id(0)
    CellText.set_property('xalign',xalign)
    treeview.append_column(output)
    return output

def AddCheckboxColumn(treeview,name,columnnumber,sortable=False,editable=None):
    CellToggle = gtk.CellRendererToggle()
    output = gtk.TreeViewColumn(name)
    output.pack_start(CellToggle,True)
    output.add_attribute(CellToggle,'active',columnnumber)
    if editable:
        CellToggle.set_property('activatable',True)
        CellToggle.connect('toggled',editable,columnnumber)
    treeview.append_column(output)
    return output
