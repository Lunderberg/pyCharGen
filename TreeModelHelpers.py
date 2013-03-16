#!/usr/bin/env python

import gtk
import gobject

class ValueListStore(gtk.ListStore,object):
    """
    Base class for StatListStore, SkillListStore, and ItemListStore.
    Subclasses should implement self.getVals(char), self.UpdateVal(valIter),
                        define cls.store_format and cls.names
                 self.getVals(char) should return an iterable of relevant items in the character
                 self.UpdateVal(valIter) should update the entry valIter in the table
                 cls.store_format should be a list of (Name,type) tuples
                 cls.names should be a dictionary from name to column number
    """
    def __init__(self,char):
        types = [t for n,t in self.store_format]
        super(ValueListStore,self).__init__(*types)
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
        for val in self.getVals(char):
            valIter = self.append()
            self.set(valIter,self.col('obj'),val)
            self.UpdateVal(valIter)
    def OnValueAdd(self,val):
        valIter = self.append()
        self.set(valIter,self.col('obj'),val)
        self.UpdateVal(valIter)
    def OnValueChange(self,val):
        for valIter in self.IterAll:
            if val is self.get(valIter,self.col('obj'))[0]:
                self.UpdateVal(valIter)
    def OnValueRemove(self,val):
        for valIter in self.IterAll:
            if val is self.get(valIter,self.col('obj'))[0]:
                self.remove(valIter)
                return

class StatListStore(ValueListStore):
    store_format = [
        ('obj',gobject.TYPE_PYOBJECT),
        ('Name',str),('Temporary',int),('SelfBonus',int),('Bonus',int)
        ]
    names = {n:i for i,(n,t) in enumerate(store_format)}
    def getVals(self,char):
        return char.Stats
    def UpdateVal(self,stIter):
        st = self.get(stIter,self.col('obj'))[0]
        self.set(stIter,
                 self.col('Name'),st.Name,
                 self.col('Temporary'),st.Value,
                 self.col('SelfBonus'),st.SelfBonus(),
                 self.col('Bonus'),st.Bonus())



class ItemListStore(ValueListStore):
    store_format = [
        ('obj',gobject.TYPE_PYOBJECT),
        ('Name',str),('Bonuses',str),('Description',str)
        ]
    names = {n:i for i,(n,t) in enumerate(store_format)}
    def getVals(self,char):
        return char.Items
    def UpdateVal(self,itIter):
        it = self.get(itIter,self.col('obj'))[0]
        name = it.Name if len(it.Name)<25 else it.Name[:25]+'...'
        bonus = it.RelativeSaveString()
        bonus = bonus if len(bonus)<25 else bonus[:25]+'...'
        descrip = it.Description if len(it.Description)<25 else it.Description[:25]+'...'
        self.set(itIter,
                 self.col('Name'),name,
                 self.col('Bonuses'),bonus,
                 self.col('Description'),descrip)

class SkillTreeStore(gtk.TreeStore,object):
    store_format = [
        ('obj',gobject.TYPE_PYOBJECT),
        ('Name',str),('Ranks',int),('SelfBonus',int),('Bonus',int),
        ('Parents',str),('CommonlyUsed',bool),('HasBonus',bool),
        ('Delta',int),('NewRanks',int),('NewSelfBonus',int),('NewBonus',int),
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
            self.set(chIter,self.col('obj'),sk)
            self.UpdateVal(chIter)
    def UpdateVal(self,skIter):
        sk = self.get(skIter,self.col('obj'))[0]
        self.set(skIter,
                 self.col('Name'),sk.Name,
                 self.col('Ranks'),sk.Value,
                 self.col('SelfBonus'),sk.SelfBonus(),
                 self.col('Bonus'),sk.Bonus(),
                 self.col('CommonlyUsed'),sk.CommonlyUsed,
                 self.col('HasBonus'),not sk.NoBonus,
                 self.col('Delta'),sk.Delta,
                 self.col('NewRanks'),sk.Value+sk.Delta,
                 self.col('NewSelfBonus'),sk.SelfBonus(levelled=True),
                 self.col('NewBonus'),sk.Bonus(levelled=True),
                 )
    def OnValueAdd(self,skill):
        pars = list(skill.Parents)
        for skIter in self.IterAll:
            if self.get(skIter,self.col('obj'))[0] in pars:
                parIter = skIter
                break
        else:
            parIter = None
        chIter = self.append(parIter)
        self.set(chIter,self.col('obj'),skill)
        self.UpdateVal(chIter)
    def OnValueChange(self,skill):
        for skIter in self.IterAll:
            if skill is self.get(skIter,self.col('obj'))[0]:
                self.UpdateVal(skIter)
    def OnValueRemove(self,skill):
        for skIter in self.IterAll:
            if skill is self.get(skIter,self.col('obj'))[0]:
                self.remove(skIter)
                return

class SkillListStore(ValueListStore):
    store_format = SkillTreeStore.store_format
    names = {n:i for i,(n,t) in enumerate(store_format)}
    def getVals(self,char):
        return char.Skills 
    UpdateVal = SkillTreeStore.__dict__['UpdateVal']

def AddTextColumn(treeview,name,columnnumber,editable=None,xalign=0.0,visible=True,viscol=None):
    CellText = gtk.CellRendererText()
    output = gtk.TreeViewColumn(name)
    output.pack_start(CellText,True)
    output.add_attribute(CellText,'text',columnnumber)
    if editable:
        CellText.set_property('editable',True)
        CellText.connect('edited',editable,columnnumber)
    CellText.set_property('xalign',xalign)
    if viscol is not None:
        output.add_attribute(CellText,'visible',viscol)
    CellText.set_visible(visible)
    treeview.append_column(output)
    return output

def AddCheckboxColumn(treeview,name,columnnumber,editable=None):
    CellToggle = gtk.CellRendererToggle()
    output = gtk.TreeViewColumn(name)
    output.pack_start(CellToggle,True)
    output.add_attribute(CellToggle,'active',columnnumber)
    if editable:
        CellToggle.set_property('activatable',True)
        CellToggle.connect('toggled',editable,columnnumber)
    treeview.append_column(output)
    return output

def RightClickToggle(treeview):
    def FromToggleColumn(menuItem,col):
        newState = menuItem.get_active()
        col.set_visible(newState)
        if not any(item.get_active() for item in menuItem.get_parent().get_children()):
            menuItem.set_active(True)
            menuItem.toggled()
    def FromHeaderClick(col):
        menu.popup(None,None,None,1,0)
    menu = gtk.Menu()
    for col in treeview.get_columns():
        menuItem = gtk.CheckMenuItem(col.get_title())
        menuItem.set_active(col.get_visible())
        menuItem.connect('toggled',FromToggleColumn,col)
        col.set_clickable(True)
        col.connect('clicked',FromHeaderClick)
        menuItem.show()
        menu.append(menuItem)
        
