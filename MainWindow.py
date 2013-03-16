#!/usr/bin/env python

import gtk
import os.path as path

import Character
import TreeModelHelpers as TMH

def better_set_text(buff,text):
    buffText = buff.get_text(buff.get_start_iter(),buff.get_end_iter())
    if buffText!=text:
        buff.set_text(text)

class MainWindow(object):
    """
    The main window of the Rolemaster GUI.
    Front tab displays the overview.
    Individual tabs for stats, skills.
    """
    def __init__(self):
        builderfile = path.join(path.dirname(__file__),
                              'glade','MainWindow.ui')

        self.registered = []
        self.char = None
        self.filename = None

        self.b = gtk.Builder()
        self.b.add_from_file(builderfile)
        self.window = self.b.get_object('mainWindow')
        self.window.connect('delete_event',gtk.main_quit)
        
        #Menu commands
        self.b.get_object('fileOpen').connect('activate',self.Open)
        self.b.get_object('fileSave').connect('activate',self.Save)
        self.b.get_object('fileSaveAs').connect('activate',self.SaveAs)
        #Updating overview text boxes
        self.b.get_object('characterName').connect('changed',self.FromNameChange)
        self.b.get_object('playerName').connect('changed',self.FromPlayerNameChange)
        self.b.get_object('experience').connect('changed',self.FromXPChange)
        #Skill right-clicking commands
        self.b.get_object('skillView').connect('button-press-event',self.FromSkillRightClick)
        self.b.get_object('rcAddChildSkill').connect('button-press-event',self.FromAddChildSkill)
        self.b.get_object('rcAddSiblingSkill').connect('button-press-event',self.FromAddSiblingSkill)
        self.b.get_object('rcDeleteSkill').connect('button-press-event',self.FromRemoveSkill)
        #Item modifying commands
        self.b.get_object('itemView').connect('button-press-event',self.FromItemRightClick)
        self.b.get_object('rcAddItem').connect('button-press-event',self.FromAddItem)
        self.b.get_object('rcDeleteItem').connect('button-press-event',self.FromRemoveItem)

        self.activeStat = None
        self.SetUpStatView()
        self.FromStatSelected()
        self.b.get_object('statView').connect('cursor-changed',self.FromStatSelected)
        self.b.get_object('statNameBox').connect('changed',self.FromActiveStatNameChange)
        self.b.get_object('statCurrentBox').connect('changed',self.FromActiveStatCurrentChange)
        self.b.get_object('statDescriptionBox').get_buffer().connect('changed',self.FromActiveStatDescriptionChange)

        self.activeSkill = None
        self.SetUpSkillView()
        self.FromSkillSelected()
        self.SetUpCommonlyUsedSkillView()
        self.b.get_object('skillView').connect('cursor-changed',self.FromSkillSelected)
        self.b.get_object('skillNameBox').connect('changed',self.FromActiveSkillNameChange)
        self.b.get_object('skillRankBox').connect('changed',self.FromActiveSkillRankChange)
        self.b.get_object('skillDescriptionBox').get_buffer().connect('changed',self.FromActiveSkillDescriptionChange)


        self.activeItem = None
        self.SetUpItemView()
        self.FromItemSelected()
        self.b.get_object('itemView').connect('cursor-changed',self.FromItemSelected)
        self.b.get_object('itemNameBox').connect('changed',self.FromActiveItemNameChange)
        self.b.get_object('itemBonusBox').connect('changed',self.FromActiveItemBonusChange)
        self.b.get_object('itemDescriptionBox').get_buffer().connect('changed',self.FromActiveItemDescriptionChange)
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
            ('Misc Changed',self.UpdateMisc),
            ('Stat Changed',self.OnStatChange),
            ('Stat Changed',self.statStore.OnValueChange),
            ('Skill Added',self.skillStore.OnValueAdd),
            ('Skill Added',self.skillListStore.OnValueAdd),
            ('Skill Changed',self.OnSkillChange),
            ('Skill Changed',self.skillStore.OnValueChange),
            ('Skill Changed',self.skillListStore.OnValueChange),
            ('Skill Removed',self.skillStore.OnValueRemove),
            ('Skill Removed',self.skillListStore.OnValueRemove),
            ('Resistance Changed',self.OnResistanceChange),
            ('Item Added',self.itemStore.OnValueAdd),
            ('Item Changed',self.OnItemChange),
            ('Item Changed',self.itemStore.OnValueChange),
            ('Item Removed',self.itemStore.OnValueRemove),
            ('Item Removed',self.OnItemRemove),
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
        self.statStore = TMH.StatListStore(self.char)
        self.statView.set_model(self.statStore)
        self.skillStore = TMH.SkillTreeStore(self.char)
        self.skillView.set_model(self.skillStore)
        self.skillListStore = TMH.SkillListStore(self.char)
        commonSkillStore = self.skillListStore.filter_new()
        commonSkillStore.set_visible_column(TMH.SkillTreeStore.col('CommonlyUsed'))
        self.commonSkillView.set_model(commonSkillStore)
        self.itemStore = TMH.ItemListStore(self.char)
        self.itemView.set_model(self.itemStore)
        self.BuildStatTable(self.char)
        self.BuildResistanceTable(self.char)
        self.UpdateMisc()
    def UpdateMisc(self,*args):
        self.b.get_object('playerName').set_text(self.char.PlayerName)
        self.b.get_object('characterName').set_text(self.char.Name)
        self.b.get_object('profName').set_text(self.char.Profession)
        self.b.get_object('raceName').set_text(self.char.Race)
        self.b.get_object('cultureName').set_text(self.char.Culture)
        self.b.get_object('charLevel').set_text(str(self.char.Level))
        self.b.get_object('experience').set_text(str(self.char.Experience))
    def SetUpStatView(self):
        """
        Builds the TreeView for the stats.
        """
        self.statView = self.b.get_object('statView')
        TMH.AddTextColumn(self.statView,'Name',TMH.StatListStore.col('Name'),
                          editable=self.FromEditStatCell)
        TMH.AddTextColumn(self.statView,'Temp',TMH.StatListStore.col('Temporary'),
                      editable=self.FromEditStatCell)
        TMH.AddTextColumn(self.statView,'Value Bonus',TMH.StatListStore.col('SelfBonus'))
        TMH.AddTextColumn(self.statView,'Bonus',TMH.StatListStore.col('Bonus'))

        TMH.RightClickToggle(self.statView)
    def SetUpSkillView(self):
        """
        Builds the TreeView for the skills.
        Also builds the right-click menu to select visible columns.
        """
        self.skillView = self.b.get_object('skillView')
        TMH.AddTextColumn(self.skillView,'Name',TMH.SkillTreeStore.col('Name'),
                            editable=self.FromEditSkillCell)
        TMH.AddTextColumn(self.skillView,'Ranks',TMH.SkillTreeStore.col('Ranks'),
                            editable=self.FromEditSkillCell,viscol=TMH.SkillTreeStore.col('HasBonus'))
        TMH.AddTextColumn(self.skillView,'Rank Bonus',TMH.SkillTreeStore.col('SelfBonus'),
                          viscol=TMH.SkillTreeStore.col('HasBonus'))
        TMH.AddTextColumn(self.skillView,'Bonus',TMH.SkillTreeStore.col('Bonus'))
        TMH.AddCheckboxColumn(self.skillView,'Commonly Used',TMH.SkillTreeStore.col('CommonlyUsed'),
                          editable=self.FromToggleSkillCell)

        TMH.RightClickToggle(self.skillView)
    def SetUpCommonlyUsedSkillView(self):
        self.commonSkillView = self.b.get_object('commonSkillView')
        TMH.AddTextColumn(self.commonSkillView,'Name',TMH.SkillTreeStore.col('Name'))
        TMH.AddTextColumn(self.commonSkillView,'Ranks',TMH.SkillTreeStore.col('Ranks'))
        TMH.AddTextColumn(self.commonSkillView,'Bonus',TMH.SkillTreeStore.col('Bonus'))
        
    def SetUpItemView(self):
        """
        Builds the TreeView for the items.
        """
        self.itemView = self.b.get_object('itemView')
        TMH.AddTextColumn(self.itemView,'Name',TMH.ItemListStore.col('Name'))
        TMH.AddTextColumn(self.itemView,'Bonuses',TMH.ItemListStore.col('Bonuses'))
        TMH.AddTextColumn(self.itemView,'Description',TMH.ItemListStore.col('Description'))

        TMH.RightClickToggle(self.itemView)
    def BuildStatTable(self,char):
        """
        Clears out and constructs the Stat table on the Overview tab.
        """
        #Clear it.
        self.statWidgets = {}
        stTable = self.b.get_object('statTable')
        for ch in stTable.get_children():
            stTable.remove(ch)
            
        #Set up the overall structure.
        length = sum(1 for _ in char.Stats)
        linesPerDivide = 5
        tableSize = 2 + length + length/linesPerDivide - (1 if length%linesPerDivide==0 else 0)
        stTable.resize(tableSize,5)
        stTable.attach(gtk.Label('Temp'),2,3,0,1)
        stTable.attach(gtk.Label('Bonus'),4,5,0,1)
        stTable.attach(gtk.HSeparator(),0,5,1,2)
        stTable.attach(gtk.VSeparator(),1,2,0,tableSize)
        stTable.attach(gtk.VSeparator(),3,4,0,tableSize)
        offset = 2
        
        #import code; code.interact(local=locals())

        #Add stat information
        for i,st in enumerate(char.Stats):
            loc = i + offset
            nameLabel = gtk.Label(st.Name)
            nameLabel.set_alignment(1.0,0.5)
            stTable.attach(nameLabel,0,1,loc,loc+1)
            tempWid = gtk.Label(str(st.Value))
            stTable.attach(tempWid,2,3,loc,loc+1)
            bonusWid = gtk.Label(str(st.Bonus()))
            stTable.attach(bonusWid,4,5,loc,loc+1)
            self.statWidgets[st.Name] = (tempWid,bonusWid)
            if (i+1) % linesPerDivide == 0 and loc+1!=tableSize:
                stTable.attach(gtk.HSeparator(),0,5,loc+1,loc+2)
                offset += 1
        stTable.show_all()
    def BuildResistanceTable(self,char):
        """
        Clears out and constructs the resistance table on the Overview tab.
        """
        self.resistanceWidgets = {}
        #Empty the table
        resTable = self.b.get_object('resistanceTable')
        for ch in resTable.get_children():
            resTable.remove(ch)
        resList = list(char.Resistances)
        resTable.resize(len(resList),2)
        for i,res in enumerate(resList):
            label = gtk.Label(res.Name + ':')
            label.set_alignment(1.0,0.5)
            value_holder = gtk.Label(str(res.Bonus()))
            resTable.attach(label,0,1,i,i+1)
            self.resistanceWidgets[res.Name] = value_holder
            resTable.attach(value_holder,1,2,i,i+1)
        resTable.show_all()
    def OnResistanceChange(self,res):
        try:
            self.resistanceWidgets[res.Name].set_text(str(res.Bonus()))
        except KeyError:
            pass
    def UpdateStat(self,stat):
        try:
            tempWid,bonusWid = self.statWidgets[stat.Name]
        except KeyError:
            return
        tempWid.set_text(str(stat.Value))
        bonusWid.set_text(str(stat.Bonus()))
    def FromEditStatCell(self,cell,path,text,col):
        st = self.statStore[path][0]
        if col==TMH.StatListStore.col('Name'):
            st.Name = text
        elif col==TMH.StatListStore.col('Temporary'):
            st.Value = int(text)
    def FromEditSkillCell(self,cell,path,text,col):
        sk = self.skillStore[path][0]
        if col==TMH.SkillTreeStore.col('Name'):
            sk.Name = text
        elif col==TMH.SkillTreeStore.col('Ranks'):
            sk.Value = int(text)
    def FromToggleSkillCell(self,cell,path,col):
        sk = self.skillStore[path][0]
        if col==TMH.SkillTreeStore.col('CommonlyUsed'):
            sk.CommonlyUsed = not sk.CommonlyUsed
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
    def FromAddChildSkill(self,*args):
        sk = self.skillStore[self.clicked_path][0]
        newSkill = Character.Skill(0,Names=['New Skill'],Options=['Skill'],Parents=[sk.Name])
        self.char.AddVal(newSkill)
    def FromAddSiblingSkill(self,*args):
        sk = self.skillStore[self.clicked_path][0]
        newSkill = Character.Skill(0,Names=['New Skill'],Options=['Skill'],Parents = [par.Name for par in sk.Parents])
        self.char.AddVal(newSkill)
    def FromRemoveSkill(self,*args):
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
    def FromStatSelected(self,*args):
        selection = self.statView.get_selection()
        model,stIter = selection.get_selected()
        if stIter is not None:
            stat = model.get(stIter,TMH.StatListStore.col('obj'))[0]
            self.activeStat = stat
            self.OnStatChange(stat)
        self.StatSensitivity()
    def StatSensitivity(self):
        for widName in ['statNameBox','statCurrentBox','statPotentialBox','statDescriptionBox']:
            wid = self.b.get_object(widName)
            wid.set_sensitive(self.activeStat is not None)
    def OnStatChange(self,stat):
        self.UpdateStat(stat)
        if stat is self.activeStat and stat is not None:
            self.b.get_object('statNameBox').set_text(stat.Name)
            self.b.get_object('statCurrentBox').set_text(str(stat.Value))
            self.b.get_object('statSelfBonusLabel').set_text(str(stat.SelfBonus()))
            self.b.get_object('statBonusLabel').set_text(str(stat.Bonus()))
            self.b.get_object('statPotentialBox').set_text('IMPLEMENT POTENTIAL')
            better_set_text(self.b.get_object('statDescriptionBox').get_buffer(),stat.Description)
    def FromSkillSelected(self,*args):
        selection = self.skillView.get_selection()
        model,skIter = selection.get_selected()
        if skIter is not None:
            skill = model.get(skIter,TMH.SkillTreeStore.col('obj'))[0]
            self.activeSkill = skill
            self.OnSkillChange(skill)
        self.SkillSensitivity()
    def SkillSensitivity(self):
        for widName in ['skillNameBox','skillDescriptionBox']:
            wid = self.b.get_object(widName)
            wid.set_sensitive(self.activeSkill is not None)
        for widName in ['skillRankBox']:
            wid = self.b.get_object(widName)
            wid.set_sensitive(self.activeSkill is not None and self.activeSkill
    def OnSkillChange(self,skill):
        if skill is self.activeSkill and skill is not None:
            self.b.get_object('skillNameBox').set_text(skill.Name)
            self.b.get_object('skillRankBox').set_text(str(skill.Value))
            self.b.get_object('skillRankBonusLabel').set_text(str(skill.SelfBonus()))
            self.b.get_object('skillCategoryBonusLabel').set_text(str(skill.CategoryBonus()))
            self.b.get_object('skillStatBonusLabel').set_text(str(skill.StatBonus()))
            self.b.get_object('skillItemBonusLabel').set_text(str(skill.ItemBonus()))
            self.b.get_object('skillBonusLabel').set_text(str(skill.Bonus()))
            better_set_text(self.b.get_object('skillDescriptionBox').get_buffer(),skill.Description)
    def OnSkillRemove(self,skill):
        self.activeSkill = None
        self.SkillSensitivity()
    def FromItemSelected(self,*args):
        selection = self.itemView.get_selection()
        model,itIter = selection.get_selected()
        if itIter is not None:
            item = model.get(itIter,TMH.ItemListStore.col('obj'))[0]
            self.activeItem = item
            self.OnItemChange(item)
        self.ItemSensitivity()
    def ItemSensitivity(self):
        for widName in ['itemNameBox','itemBonusBox','itemDescriptionBox']:
            wid = self.b.get_object(widName)
            wid.set_sensitive(self.activeItem is not None)
    def OnItemChange(self,item):
        if item is self.activeItem and item is not None:
            self.b.get_object('itemNameBox').set_text(item.Name)
            self.b.get_object('itemBonusBox').set_text(item.RelativeSaveString())
            better_set_text(self.b.get_object('itemDescriptionBox').get_buffer(),item.Description)
    def OnItemRemove(self,item):
        self.activeItem = None
        self.ItemSensitivity()
    def FromItemRightClick(self,widget,event):
        if event.button==3:
            path = widget.get_path_at_pos(int(event.x),int(event.y))
            if path is None:
                self.clicked_item = None
            else:
                path = path[0]
                self.clicked_item = self.itemStore[path][0]
            self.b.get_object('rcItemMenu').popup(
                None,None,None,event.button,event.time)
    def FromAddItem(self,*args):
        newItem = Character.Item(None,Names=['New Item'],Options=['Item'])
        self.char.AddVal(newItem)
    def FromRemoveItem(self,*args):
        if self.clicked_item is None:
            return
        dialog = gtk.Dialog('Are you sure?', self.window,
                            gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                            (gtk.STOCK_NO,gtk.RESPONSE_CANCEL,
                             gtk.STOCK_YES,gtk.RESPONSE_OK))
        dialog.vbox.pack_start(gtk.Label("Are you sure you want to delete '{0}'".format(self.clicked_item.Name)))
        dialog.show_all()
        result = dialog.run()
        dialog.destroy()
        if result==gtk.RESPONSE_OK:
            self.char.RemoveVal(self.clicked_item)
    def FromActiveStatNameChange(self,widget):
        if self.activeStat is not None:
            self.activeStat.Name = widget.get_text()
    def FromActiveStatCurrentChange(self,widget):
        if self.activeStat is not None:
            try:
                self.activeStat.Value = int(widget.get_text())
            except ValueError:
                pass
    def FromActiveStatDescriptionChange(self,widget):
        if self.activeStat is not None:
            text = widget.get_text(widget.get_start_iter(),widget.get_end_iter())
            self.activeStat.Description = text
    def FromActiveSkillNameChange(self,widget):
        if self.activeSkill is not None:
            self.activeSkill.Name = self.b.get_object('skillNameBox').get_text()
    def FromActiveSkillRankChange(self,widget):
        if self.activeSkill is not None:
            try:
                self.activeSkill.Value = int(widget.get_text())
            except ValueError:
                pass
    def FromActiveSkillDescriptionChange(self,widget):
        if self.activeSkill is not None:
            text = widget.get_text(widget.get_start_iter(),widget.get_end_iter())
            self.activeSkill.Description = text
    def FromActiveItemNameChange(self,widget):
        if self.activeItem is not None:
            self.activeItem.Name = widget.get_text()
    def FromActiveItemBonusChange(self,widget):
        if self.activeItem is not None:
            self.activeItem.ChangeBonuses(widget.get_text())
    def FromActiveItemDescriptionChange(self,widget):
        if self.activeItem is not None:
            self.activeItem.Description = widget.get_text(widget.get_start_iter(),
                                                          widget.get_end_iter())
                
        

if __name__=='__main__':
    gui = MainWindow()
    gui.Show()
    gtk.main()
