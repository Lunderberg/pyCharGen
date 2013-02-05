#!/usr/bin/env python

import gtk
import os.path as path

import Character
from TreeModelHelpers import StatStore,SkillStore,AddTextColumn,AddCheckboxColumn

class MainWindow(object):
    """
    The main window of the Rolemaster GUI.
    Front tab displays the overview.
    Individual tabs for stats, skills.
    """
    def __init__(self):
        builderfile = path.join(path.dirname(__file__),
                              'glade','MainWindow.builder')

        self.registered = []
        self.char = None
        self.filename = None

        self.b = gtk.Builder()
        self.b.add_from_file(builderfile)
        self.window = self.b.get_object('mainWindow')
        self.window.connect('delete_event',gtk.main_quit)
        
        self.b.get_object('fileOpen').connect('activate',self.Open)
        self.b.get_object('fileSave').connect('activate',self.Save)
        self.b.get_object('fileSaveAs').connect('activate',self.SaveAs)
        self.b.get_object('characterName').connect('changed',self.FromNameChange)
        self.b.get_object('playerName').connect('changed',self.FromPlayerNameChange)
        self.b.get_object('experience').connect('changed',self.FromXPChange)
        self.b.get_object('skillView').connect('button-press-event',self.FromSkillRightClick)
        self.b.get_object('rcAddSkill').connect('button-press-event',self.FromAddSkill)
        self.b.get_object('rcDeleteSkill').connect('button-press-event',self.FromRemoveSkill)
        self.SetUpStatView()
        self.SetUpSkillView()
    def Show(self):
        self.window.show_all()
    def Hide(self):
        self.window.hide()
    def Open(self,*args):
        """
        Displays a dialog to choose a character file.
        If selected, will call LoadChar() with the new character.
        """
        t = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_OPEN,
                                  buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,
                                           gtk.STOCK_OPEN,gtk.RESPONSE_OK))
        response = t.run()
        filename = t.get_filename()
        t.destroy()
        if response==gtk.RESPONSE_OK:
            char = Character.Character.Open(filename)
            self.filename = filename
            self.LoadChar(char)
    def LoadChar(self,char):
        """
        Removes any registered functions from the old character, if any.
        Calls UpdateAll() and registers update functions with the new character.
        """
        #Clear out any functions from previous character in its EventHandler.
        if self.char is not None:
            for key,func in self.registered:
                self.char.Events.Remove(key,func)
        #Load the character.
        self.char = char
        self.UpdateAll()
        #Register the updating functions
        self.registered = [
            ('Stat Changed',self.statStore.OnStatChange),
            ('Stat Changed',self.statStore.UpdateStat),
            ('Skill Changed',self.skillStore.OnSkillChange),
            ('Resistance Changed',self.OnResistanceChange),
            ('Skill Removed',self.skillStore.OnSkillRemove)
            ]
        for key,func in self.registered:
            self.char.Events.Register(key,func)
    def Save(self,*args):
        """
        Saves to the most recently selected file, either from Open() or SaveAs()
        """
        if self.filename is not None:
            with open(filename,'w') as f:
                f.write(self.char.SaveString())
    def SaveAs(self,*args):
        """
        Saves to a selected file.
        """
        t = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_SAVE,
                                  buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,
                                           gtk.STOCK_OPEN,gtk.RESPONSE_OK))
        response = t.run()
        filename = t.get_filename()
        t.destroy()
        if response==gtk.RESPONSE_OK:
            with open(filename,'w') as f:
                f.write(self.char.SaveString())
            self.filename = filename
    def UpdateAll(self,*args):
        """
        Refreshes all character information from self.char.
        A bit drastic of a modification unless loading a new character.
        Rebuilds self.statStore and self.skillStore.
        Rebuilds table of resistances.
        """
        for st in self.char.Stats:
            self.UpdateStat(st)
        self.statStore = StatStore(self.char)
        self.statView.set_model(self.statStore)
        self.skillStore = SkillStore(self.char)
        self.skillView.set_model(self.skillStore)
        self.BuildResistanceTable(self.char)
    def SetUpStatView(self):
        """
        Builds the TreeView for the stats.
        """
        self.statView = self.b.get_object('statView')
        AddTextColumn(self.statView,'Name',StatStore.col('Name'))
        AddTextColumn(self.statView,'Temp',StatStore.col('Temporary'),
                      editable=self.FromEditStatCell)
        AddTextColumn(self.statView,'SelfBonus',StatStore.col('SelfBonus'))
        AddTextColumn(self.statView,'Bonus',StatStore.col('Bonus'))
    def SetUpSkillView(self):
        """
        Builds the TreeView for the skills.
        """
        self.skillView = self.b.get_object('skillView')
        AddTextColumn(self.skillView,'Name',SkillStore.col('Name'))
        AddTextColumn(self.skillView,'Ranks',SkillStore.col('Ranks'),
                      editable=self.FromEditSkillCell)
        AddTextColumn(self.skillView,'Rank Bonus',SkillStore.col('SelfBonus'))
        AddTextColumn(self.skillView,'Bonus',SkillStore.col('Bonus'))
    def BuildResistanceTable(self,char):
        self.resistanceWidgets = {}
        #Empty the table
        resTable = self.b.get_object('resistanceTable')
        for ch in resTable.get_children():
            resTable.remove(ch)
        resList = list(char.Resistances)
        resTable.resize(len(resList),2)
        for i,res in enumerate(resList):
            label = gtk.Label(res.Name + ':')
            value_holder = gtk.Label(str(res.Bonus))
            resTable.attach(label,0,1,i,i+1)
            self.resistanceWidgets[res.Name] = value_holder
            resTable.attach(value_holder,1,2,i,i+1)
        resTable.show_all()
    def OnResistanceChange(self,res):
        try:
            self.resistanceWidgets[res.Name].set_text(str(res.Bonus))
        except KeyError:
            pass
    def UpdateStat(self,stat):
        wid = self.b.get_object(stat.Name+"Temp")
        if wid is not None:
            wid.set_text(str(stat.Value))
        wid = self.b.get_object(stat.Name+"Bonus")
        if wid is not None:
            wid.set_text(str(stat.Bonus))
    def FromEditStatCell(self,cell,path,text,col):
        st = self.statStore[path][0]
        if col==StatStore.col('Temporary'):
            st.Value = int(text)
    def FromEditSkillCell(self,cell,path,text,col):
        sk = self.skillStore[path][0]
        if col==SkillStore.col('Ranks'):
            sk.Value = int(text)
    def FromSkillRightClick(self,widget,event):
        if event.button==3: #Right-click
            path = widget.get_path_at_pos(int(event.x),int(event.y))
            if path is None:
                return
            path = path[0]
            widget.set_cursor(path)
            self.clicked_path = path
            self.b.get_object('rcSkillMenu').popup(
                None,None,None,event.button,event.time)
    def FromAddSkill(self,*args):
        pass
    def FromRemoveSkill(self,widget,event):
        sk = self.skillStore[self.clicked_path][0]
        dialog = gtk.Dialog('Are you sure?', self.window,
                            gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                            (gtk.STOCK_NO,gtk.RESPONSE_CANCEL,
                             gtk.STOCK_YES,gtk.RESPONSE_OK))
        dialog.vbox.pack_start(gtk.Label("Are you sure you want to delete '{0}'".format(sk.Name)))
        dialog.show_all()
        result = dialog.run()
        dialog.destroy()
        if result==gtk.RESPONSE_OK:
            self.char.RemoveVal(sk)
    def FromNameChange(self,widget):
        self.char.Name = widget.get_text()
    def FromPlayerNameChange(self,widget):
        self.char.PlayerName = widget.get_text()
    def FromXPChange(self,widget):
        try:
            self.char.XP = int(widget.get_text())
        except ValueError:
            pass
        

if __name__=='__main__':
    gui = MainWindow()
    gui.Show()
    gtk.main()
