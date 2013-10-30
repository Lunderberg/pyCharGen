#!/usr/bin/env python

import gtk
import os.path
import sys

from backend import Character
from backend import Parser
from backend.utils import resource

from gui import TreeModelHelpers as TMH
from gui import LatexOutput
from gui import CultureWindow

#Load the gtk theme for windows.
#Should this at some point no longer be the main script,
#  move this to be in the main script.
if (sys.platform=='win32') and hasattr(sys,'_MEIPASS'):
    basedir = sys._MEIPASS
    gtkrc = os.path.join(basedir,'gtkrc')
    gtk.rc_set_default_files([gtkrc])
    gtk.rc_reparse_all_for_settings(gtk.settings_get_default(),True)

def better_set_text(buff,text):
    buffText = buff.get_text(buff.get_start_iter(),buff.get_end_iter())
    if buffText!=text:
        buff.set_text(text)

def combobox_boilerplate(combobox):
    store = gtk.ListStore(str)
    combobox.set_model(store)
    cell = gtk.CellRendererText()
    combobox.pack_start(cell,True)
    combobox.add_attribute(cell,'text',0)

class MainWindow(object):
    """
    The main window of the Rolemaster GUI.
    Front tab displays the overview.
    Individual tabs for stats, skills.
    """
    def __init__(self):
        builderfile = resource('resources','MainWindow.ui')
        self.char = None
        self.changed_since_save = False

        self.b = gtk.Builder()
        self.b.add_from_file(builderfile)
        self.window = self['mainWindow']
        self.window.connect('delete_event',self.Exit)

        #Menu commands
        self.Connect(self['fileNew'],'activate',self.New)
        self.Connect(self['fileOpen'],'activate',self.Open)
        self.Connect(self['fileSave'],'activate',self.Save)
        self.Connect(self['fileSaveAs'],'activate',self.SaveAs)
        self.Connect(self['fileExport'],'activate',self.Export)
        self.Connect(self['fileQuit'],'activate',self.Exit)
        self.Connect(self['actionLevelUp'],'activate',self.FromLevelUp)
        #The About window.
        self.Connect(self['helpAbout'],'activate',self.ShowAbout)
        self.Connect(self['aboutWindow'],'delete_event',self.HideAbout)
        self.Connect(self['aboutOkay'],'clicked',self.HideAbout)
        #Updating overview text boxes
        self.Connect(self['characterName'],'changed',self.FromNameChange)
        self.Connect(self['playerName'],'changed',self.FromPlayerNameChange)
        self.Connect(self['experience'],'changed',self.FromXPChange)
        #Skill right-clicking commands
        self.Connect(self['skillView'],'button-press-event',self.FromSkillRightClick)
        self.Connect(self['rcAddChildSkill'],'button-press-event',self.FromAddChildSkill)
        self.Connect(self['rcAddSiblingSkill'],'button-press-event',self.FromAddSiblingSkill)
        self.Connect(self['rcDeleteSkill'],'button-press-event',self.FromRemoveSkill)
        #Item modifying commands
        self.Connect(self['itemView'],'button-press-event',self.FromItemRightClick)
        self.Connect(self['rcAddItem'],'button-press-event',self.FromAddItem)
        self.Connect(self['rcDeleteItem'],'button-press-event',self.FromRemoveItem)

        #Stat modifications.
        self.activeStat = None
        self.SetUpStatView()
        self.FromStatSelected()
        self.Connect(self['statView'],'cursor-changed',self.FromStatSelected)
        self.Connect(self['statNameBox'],'changed',self.FromActiveStatNameChange)
        self.Connect(self['statCurrentBox'],'changed',self.FromActiveStatCurrentChange)
        self.Connect(self['statPotentialBox'],'changed',self.FromActiveStatPotentialChange)
        self.Connect(self['statDescriptionBox'].get_buffer(),
                     'changed',self.FromActiveStatDescriptionChange)
        self.Connect(self['levellingStatGain'],'changed',self.FromActiveStatLevellingChange)
        self.Connect(self['levellingStatGain'],'value-changed',self.FromActiveStatLevellingChange)

        #Skill modifications
        self.activeSkill = None
        self.SetUpSkillView()
        self.FromSkillSelected()
        self.SetUpCommonlyUsedSkillView()
        self.Connect(self['skillView'],'cursor-changed',self.FromSkillSelected)
        self.Connect(self['skillNameBox'],'changed',self.FromActiveSkillNameChange)
        self.Connect(self['skillRankBox'],'changed',self.FromActiveSkillRankChange)
        self.Connect(self['skillDescriptionBox'].get_buffer(),
                     'changed',self.FromActiveSkillDescriptionChange)

        #Weapon reorderings
        self.SetUpWeaponSkillView()

        #Item modifications
        self.activeItem = None
        self.SetUpItemView()
        self.FromItemSelected()
        self.Connect(self['itemView'],'cursor-changed',self.FromItemSelected)
        self.Connect(self['itemNameBox'],'changed',self.FromActiveItemNameChange)
        self.Connect(self['itemBonusBox'],'changed',self.FromActiveItemBonusChange)
        self.Connect(self['itemEnabledButton'],'toggled',self.FromActiveItemEnabledChange)
        self.Connect(self['itemDescriptionBox'].get_buffer(),'changed',self.FromActiveItemDescriptionChange)

        #Profession setup
        self.MakeProfessionList()
        self.Connect(self['profBox'],'changed',self.FromProfessionSelect)

        #Culture setup
        self.MakeCultureList()
        self.Connect(self['cultureBox'],'changed',self.FromCultureSelect)

        #Race setup
        self.MakeRaceList()
        self.Connect(self['raceBox'],'changed',self.FromRaceSelect)

        #Set up a default character.
        self.registered = []
        self.LoadFile(resource('tables','BaseChar.txt'))
        self.filename = None

    def __getitem__(self,key):
        return self.b.get_object(key)
    def Connect(self,wid,sig,hand,*args):
        if not hasattr(self,'_handlers'):
            self._handlers = []
        hand_id = wid.connect(sig,hand,*args)
        self._handlers.append( (wid,hand_id) )
        if hasattr(self,'_blocked') and self._blocked:
            wid.handler_block(hand_id)
    def Disconnect(self,wid):
        """
        Disconnects all signals coming from the specified widget.
        """
        for widtest,hand_id in self._handlers:
            if widtest is wid:
                wid.disconnect(hand_id)
        self._handlers = [(w,h) for w,h in self._handlers if (w is not wid)]
    def Block(self):
        for wid,handler_id in self._handlers:
            wid.handler_block(handler_id)
        self._blocked = True
    def Unblock(self):
        for wid,handler_id in self._handlers:
            wid.handler_unblock(handler_id)
        self._blocked = False
    def Update(self):
        if self.char is None:
            return
        self.changed_since_save = True
        self.Block()
        self.char.Update()
        self.Unblock()
    def Show(self):
        self.window.show_all()
        self.ShowHideLevelling()
    def Hide(self):
        self.window.hide()
    def ShowAbout(self,*args):
        self['aboutWindow'].show_all()
    def HideAbout(self,*args):
        self['aboutWindow'].hide()
        return True
    def New(self,*args):
        self.LoadFile(resource('tables','BaseChar.txt'))
        self['mainTabs'].set_current_page(1)
        self.changed_since_save = False
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
            self.LoadFile(filename)
    def LoadFile(self,filename):
        char = Character.Character.Open(filename)
        self.filename = filename
        self.LoadChar(char)
        self.changed_since_save = False
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
            ('Skill Added',self.weaponSkillStore.OnValueAdd),
            ('Skill Changed',self.OnSkillChange),
            ('Skill Changed',self.skillStore.OnValueChange),
            ('Skill Changed',self.skillListStore.OnValueChange),
            ('Skill Changed',self.weaponSkillStore.OnValueChange),
            ('Skill Removed',self.skillStore.OnValueRemove),
            ('Skill Removed',self.skillListStore.OnValueRemove),
            ('Skill Removed',self.weaponSkillStore.OnValueRemove),
            ('Resistance Changed',self.OnResistanceChange),
            ('Item Added',self.itemStore.OnValueAdd),
            ('Item Changed',self.itemStore.OnValueChange),
            ('Item Removed',self.itemStore.OnValueRemove),
            ('Item Removed',self.OnItemRemove),
            ('Culture Added',self.OnCultureChange),
            ('Race Added',self.OnRaceChange),
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
            self.changed_since_save = False
        else:
            self.SaveAs()
    def SaveAs(self,*args):
        """
        Saves to a selected file.
        """
        t = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_SAVE,
                                  buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,
                                           gtk.STOCK_SAVE,gtk.RESPONSE_OK))
        response = t.run()
        filename = t.get_filename()
        t.destroy()
        if response==gtk.RESPONSE_OK:
            with open(filename,'w') as f:
                f.write(self.char.SaveString())
            self.filename = filename
            self.changed_since_save = False
    def Export(self,*args):
        """
        Exports the character either to a pdf, or to a .tex file.
        """
        t = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_SAVE,
                                  buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,
                                           gtk.STOCK_SAVE,gtk.RESPONSE_OK))
        t.set_current_name(self.char.GetMisc('Name')+'.pdf'
                           if self.char.GetMisc('Name')
                           else 'char.pdf')
        response = t.run()
        filename = t.get_filename()
        t.destroy()
        if response==gtk.RESPONSE_OK:
            if filename[-4:]!='.pdf':
                filename += '.pdf'
            LatexOutput.CompileLatex(self.char,filename)
    def OkayWithoutSaving(self):
        """
        If nothing has changed, return True.
        Otherwise, query the user and ask whether it is okay to exit.
        """
        if not self.changed_since_save:
            return True
        t = gtk.Dialog("Are you sure?",self.window,
                       gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                       (gtk.STOCK_YES,gtk.RESPONSE_OK,
                        gtk.STOCK_NO,gtk.RESPONSE_CANCEL))
        t.vbox.pack_start(gtk.Label("There is unsaved work.\nDo you want to quit?"))
        t.vbox.show_all()
        response = t.run()
        t.destroy()
        return response==gtk.RESPONSE_OK
    def Exit(self,*args):
        if self.OkayWithoutSaving():
            gtk.main_quit()
            return False
        else:
            return True
    def MakeProfessionList(self):
        self._profdict = Parser.LoadProfessions(resource('tables','Professions.txt'))
        profBox = self['profBox']
        combobox_boilerplate(profBox)
        for key in self._profdict:
            profBox.append_text(key)
    def FromProfessionSelect(self,wid):
        profname = wid.get_active_text()
        self.char.LoadProfession(profname,self._profdict[profname])
        self.Update()
    def MakeCultureList(self):
        self._cultureList = Parser.cultureFile(resource('tables','Cultures.txt'))
        cultureBox = self['cultureBox']
        combobox_boilerplate(cultureBox)
        for proto in self._cultureList:
            cultureBox.append_text(proto.Name)
    def FromCultureSelect(self,*args):
        selection = self['cultureBox'].get_active()
        prototype = self._cultureList[selection]
        prototype.char = self.char
        subwindow = CultureWindow.CultureWindow(prototype,self.PostCultureCustomization)
        subwindow.Show()
        self.Hide()
    def PostCultureCustomization(self,gtkWindow,gtkEvent,subwindow):
        self.char.Culture = subwindow.Culture
        self.Show()
        subwindow.window.destroy()
        self.Update()
    def MakeRaceList(self):
        self._racelist = Parser.raceFile(resource('tables','Races.txt'))
        raceBox = self['raceBox']
        combobox_boilerplate(raceBox)
        for race in self._racelist:
            raceBox.append_text(race.Name)
    def FromRaceSelect(self,*args):
        selection = self['raceBox'].get_active()
        self.char.Race = self._racelist[selection]
        self.Update()
    def UpdateAll(self,*args):
        """
        Refreshes all character information from self.char.
        A bit drastic of a modification unless loading a new character.
        Rebuilds self.statStore and self.skillStore.
        Rebuilds table of resistances.
        """
        self.Block()
        self.statStore = TMH.StatListStore(self.char)
        self.statView.set_model(self.statStore)
        self.skillStore = TMH.SkillTreeStore(self.char)
        self.skillView.set_model(self.skillStore)
        self.skillListStore = TMH.SkillListStore(self.char)
        commonSkillStore = self.skillListStore.filter_new()
        commonSkillStore.set_visible_column(TMH.SkillTreeStore.col('CommonlyUsed'))
        self.commonSkillView.set_model(commonSkillStore)
        if hasattr(self,'weaponSkillStore'):
            self.Disconnect(self.weaponSkillStore)
        self.weaponSkillStore = TMH.WeaponListStore(self.char)
        self.weaponSkillView.set_model(self.weaponSkillStore)
        #rows-reordered does nothing, and row-inserted still keeps the old row on.
        #row-deleted is called last whenever a row is moved.
        self.Connect(self.weaponSkillStore,'row-deleted',self.FromWeaponReorder)
        self.itemStore = TMH.ItemListStore(self.char)
        self.itemView.set_model(self.itemStore)
        self.BuildStatTable(self.char)
        self.BuildResistanceTable(self.char)
        self.UpdateMisc()
        self.ShowHideLevelling()
        self.Unblock()
    def UpdateMisc(self,*args):
        self['playerName'].set_text(self.char.GetMisc('PlayerName'))
        self['characterName'].set_text(self.char.GetMisc('Name'))
        self['profName'].set_text(self.char.GetMisc('Profession'))
        self['raceName'].set_text(self.char.Race.Name if self.char.Race is not None else '')
        self['cultureName'].set_text(self.char.Culture.Name if self.char.Culture is not None else '')
        self['charLevel'].set_text(str(self.char.GetMisc('Level')))
        self['experience'].set_text(str(self.char.GetMisc('Experience')))
    def SetUpStatView(self):
        """
        Builds the TreeView for the stats.
        """
        self.statView = self['statView']
        TMH.AddTextColumn(self.statView,'Name',TMH.StatListStore.col('Name'),
                          editable=self.FromEditStatCell)
        TMH.AddTextColumn(self.statView,'Temp',TMH.StatListStore.col('Temporary'),
                          editable=self.FromEditStatCell)
        TMH.AddTextColumn(self.statView,'Value Bonus',TMH.StatListStore.col('ValueBonus'))
        TMH.AddTextColumn(self.statView,'Potential',TMH.StatListStore.col('Potential'),
                          editable=self.FromEditStatCell)
        TMH.AddTextColumn(self.statView,'Potential Bonus',TMH.StatListStore.col('PotentialBonus'))
        TMH.AddTextColumn(self.statView,'Bonus',TMH.StatListStore.col('Bonus'))

        TMH.RightClickToggle(self.statView)
    def SetUpSkillView(self):
        """
        Builds the TreeView for the skills.
        Also builds the right-click menu to select visible columns.
        """
        self.skillView = self['skillView']
        TMH.AddTextColumn(self.skillView,'Name',TMH.SkillTreeStore.col('Name'),
                            editable=self.FromEditSkillCell)
        TMH.AddTextColumn(self.skillView,'Ranks',TMH.SkillTreeStore.col('Ranks'),
                            editable=self.FromEditSkillCell,viscol=TMH.SkillTreeStore.col('HasBonus'))
        TMH.AddTextColumn(self.skillView,'Rank Bonus',TMH.SkillTreeStore.col('ValueBonus'),
                          viscol=TMH.SkillTreeStore.col('HasBonus'))
        TMH.AddTextColumn(self.skillView,'Bonus',TMH.SkillTreeStore.col('Bonus'))
        TMH.AddCheckboxColumn(self.skillView,'Commonly Used',TMH.SkillTreeStore.col('CommonlyUsed'),
                          editable=self.FromToggleSkillCell)

        TMH.RightClickToggle(self.skillView)
    def SetUpCommonlyUsedSkillView(self):
        self.commonSkillView = self['commonSkillView']
        TMH.AddTextColumn(self.commonSkillView,'Name',TMH.SkillTreeStore.col('Name'))
        TMH.AddTextColumn(self.commonSkillView,'Ranks',TMH.SkillTreeStore.col('Ranks'))
        TMH.AddTextColumn(self.commonSkillView,'Bonus',TMH.SkillTreeStore.col('Bonus'))
    def SetUpWeaponSkillView(self):
        self.weaponSkillView = self['weaponOrderingView']
        TMH.AddTextColumn(self.weaponSkillView,'Name',TMH.SkillTreeStore.col('Name'))
        self.weaponSkillView.set_reorderable(True)
    def FromWeaponReorder(self,wid,*args):
        self.char.WeaponList = wid.OrderedSkills()
        self.Update()
    def SetUpItemView(self):
        """
        Builds the TreeView for the items.
        """
        self.itemView = self['itemView']
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
        stTable = self['statTable']
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
        resTable = self['resistanceTable']
        for ch in resTable.get_children():
            resTable.remove(ch)
        resList = list(char.Resistances)
        if not resList:
            return
        resTable.resize(len(resList),2)
        for i,res in enumerate(resList):
            label = gtk.Label(res.Name + ':')
            label.set_alignment(1.0,0.5)
            value_holder = gtk.Label(str(res.Bonus()))
            resTable.attach(label,0,1,i,i+1)
            self.resistanceWidgets[res.Name] = value_holder
            resTable.attach(value_holder,1,2,i,i+1)
        resTable.show_all()
    def ShowHideLevelling(self):
        """
        Shows or hide widgets based on the current character state.
        Character starting information should not be present once hitting level 1.
        Likewise, levelling-up information should not be present until hitting level 1.
        """
        if self.char is None:
            return
        level = self.char.GetMisc('Level')
        if level==0:
            self['statLevellingUpFrame'].hide()
            self['mainTabs'].get_nth_page(1).show()
            self['startStatFrame'].show()
        else:
            self['statLevellingUpFrame'].show()
            self['mainTabs'].get_nth_page(1).hide()
            self['startStatFrame'].hide()
    def OnResistanceChange(self,res):
        try:
            self.resistanceWidgets[res.Name].set_text(str(res.Bonus()))
        except KeyError:
            pass
    def UpdateStatOverview(self,stat):
        try:
            tempWid,bonusWid = self.statWidgets[stat.Name]
        except KeyError:
            return
        tempWid.set_text(str(stat.Value))
        bonusWid.set_text(str(stat.Bonus()))
    def UpdateActiveStat(self,stat):
        self['statNameBox'].set_text(stat.Name)
        self['statCurrentBox'].set_text(str(stat.Value))
        self['statValueBonusLabel'].set_text(str(stat.ValueBonus()))
        self['statBonusLabel'].set_text(str(stat.Bonus()))
        self['statPotentialBox'].set_text(str(stat.Max))
        better_set_text(self['statDescriptionBox'].get_buffer(),stat.Description)
        adj = self['levellingStatGain']
        adj.set_lower(0)
        adj.set_upper(100-stat.Value)
        adj.set_value(stat.Delta)
        self['postLevelStatBonus'].set_text(str(stat.ValueBonus(levelled=True)))
    def UpdateActiveSkill(self,skill):
        self['skillNameBox'].set_text(skill.Name)
        self['skillRankBox'].set_text(str(skill.Value))
        self['skillRankBonusLabel'].set_text(str(skill.ValueBonus()))
        self['skillCategoryBonusLabel'].set_text(str(skill.CategoryBonus()))
        self['skillStatBonusLabel'].set_text(str(skill.StatBonus()))
        self['skillItemBonusLabel'].set_text(str(skill.ItemBonus()))
        self['skillBonusLabel'].set_text(str(skill.Bonus()))
        better_set_text(self['skillDescriptionBox'].get_buffer(),skill.Description)
        self.BuildRanksButtons(skill)
        self['postLevelSkillRanks'].set_text(str(skill.Value+skill.Delta))
        self['postLevelSkillBonus'].set_text(str(skill.ValueBonus(levelled=True)))
    def BuildRanksButtons(self,skill):
        """
        Builds the buttons to be pressed to select the skill ranks to be bought.
        Currently, is called whenever the active skill changes.
        Rather overkill to destroy and rebuild the buttons each time,
             and I might simplify it later.
        """
        if not hasattr(self,'_rankButtonHandlers'):
            self._rankButtonHandlers = []
        box = self['skillRanksButtonBox']
        for handler,button in self._rankButtonHandlers:
            button.disconnect(handler)
            box.remove(button)
        self._rankButtonHandlers = []
        if not skill.NoBonus:
            for i,cost in enumerate(skill.Costs):
                button = gtk.ToggleButton(str(cost))
                button.set_active((i+1)<=skill.Delta)
                box.pack_start(button)
                button.show()
                handler = button.connect('toggled',self.FromRankButtonToggle,i+1)
                self._rankButtonHandlers.append((handler,button))
    def FromRankButtonToggle(self,button,ranks):
        if self.activeSkill is not None:
            self.activeSkill.Delta = ranks + (0 if button.get_active() else -1)
        self.Update()
    def FromEditStatCell(self,cell,path,text,col):
        st = self.statStore[path][0]
        if col==TMH.StatListStore.col('Name'):
            st.Name = text
        elif col==TMH.StatListStore.col('Temporary'):
            st.Value = int(text)
        elif col==TMH.StatListStore.col('Potential'):
            st.Max = int(text)
        self.Update()
    def FromEditSkillCell(self,cell,path,text,col):
        sk = self.skillStore[path][0]
        if col==TMH.SkillTreeStore.col('Name'):
            sk.Name = text
        elif col==TMH.SkillTreeStore.col('Ranks'):
            sk.Value = int(text)
        self.Update()
    def FromToggleSkillCell(self,cell,path,col):
        sk = self.skillStore[path][0]
        if col==TMH.SkillTreeStore.col('CommonlyUsed'):
            sk.CommonlyUsed = not sk.CommonlyUsed
        self.Update()
    def FromSkillRightClick(self,widget,event):
        if event.button==3: #Right-click
            path = widget.get_path_at_pos(int(event.x),int(event.y))
            if path is None:
                return
            path = path[0]
            widget.set_cursor(path)
            self.clicked_path = path
            self['rcSkillMenu'].popup(
                None,None,None,event.button,event.time)
    def FromAddChildSkill(self,*args):
        sk = self.skillStore[self.clicked_path][0]
        newSkill = Character.Skill(0,Names=['New Skill'],Options=['Skill'],Parents=[sk])
        self.char.AddVal(newSkill)
        self.Update()
    def FromAddSiblingSkill(self,*args):
        sk = self.skillStore[self.clicked_path][0]
        newSkill = Character.Skill(0,Names=['New Skill'],Options=['Skill'],Parents = [par.Name for par in sk.Parents])
        self.char.AddVal(newSkill)
        self.Update()
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
        self.Update()
    def FromNameChange(self,widget):
        self.char.SetMisc('Name',widget.get_text())
        self.Update()
    def FromPlayerNameChange(self,widget):
        self.char.SetMisc('PlayerName',widget.get_text())
        self.Update()
    def FromXPChange(self,widget):
        try:
            self.char.SetMisc('Experience',int(widget.get_text()))
        except ValueError:
            pass
        self.Update()
    def FromStatSelected(self,*args):
        selection = self.statView.get_selection()
        model,stIter = selection.get_selected()
        if stIter is not None:
            stat = model.get(stIter,TMH.StatListStore.col('obj'))[0]
            self.activeStat = stat
            self.Block()
            self.OnStatChange(stat)
            self.Unblock()
        self.StatSensitivity()
    def StatSensitivity(self):
        for widName in ['statNameBox','statCurrentBox','statPotentialBox','statDescriptionBox']:
            wid = self[widName]
            wid.set_sensitive(self.activeStat is not None)
    def OnRaceChange(self,race):
        self['raceName'].set_text(race.Name)
    def OnCultureChange(self,culture):
        self['cultureName'].set_text(culture.Name)
    def OnStatChange(self,stat):
        self.UpdateStatOverview(stat)
        if stat is self.activeStat and stat is not None:
            self.UpdateActiveStat(stat)
        try:
            self['SPspentLabel'].set_text('Stat Points Spent: {0}/{1}'.format(
                    self.char.StatPoints(levelled=True)-self.char.StatPoints(),
                    self.char.StatPointsAllowed()))
        except KeyError as e:
            print "Unknown stat value: ",e.args[1]
        try:
            self['potlSPspent'].set_text("Pot'l Stat Points Spent: {0}/{1}".format(
                    self.char.StatPoints(potl=True), self.char.StatPointsAllowed(potl=True)))
        except KeyError as e:
            print "Unknown stat value: ",e.args[1]
        try:
            self['initSPspent'].set_text("Stat Points Spent: {0}/{1}".format(
                    self.char.StatPoints(), self.char.StatPointsAllowed()))
        except KeyError as e:
            print "Unknown stat value: ",e.args[1]
    def FromSkillSelected(self,*args):
        selection = self.skillView.get_selection()
        model,skIter = selection.get_selected()
        if skIter is not None:
            skill = model.get(skIter,TMH.SkillTreeStore.col('obj'))[0]
            self.activeSkill = skill
            self.Block()
            self.OnSkillChange(skill)
            self.Unblock()
        self.SkillSensitivity()
    def SkillSensitivity(self):
        for widName in ['skillNameBox','skillDescriptionBox']:
            wid = self[widName]
            wid.set_sensitive(self.activeSkill is not None)
        for widName in ['skillRankBox']:
            wid = self[widName]
            wid.set_sensitive(self.activeSkill is not None and
                              not self.activeSkill.NoBonus)
    def OnSkillChange(self,skill):
        if skill is self.activeSkill and skill is not None:
            self.UpdateActiveSkill(skill)
        self['DPspentLabel'].set_text('Development Points Spent: {0}/{1}'.format(
                self.char.DPspent(), self.char.DPallowed()))
    def OnSkillRemove(self,skill):
        self.activeSkill = None
        self.SkillSensitivity()
    def FromItemSelected(self,*args):
        selection = self.itemView.get_selection()
        model,itIter = selection.get_selected()
        if itIter is not None:
            item = model.get(itIter,TMH.ItemListStore.col('obj'))[0]
            self.activeItem = item
            self.Block()
            self.OnItemChange(item)
            self.Unblock()
        self.ItemSensitivity()
    def ItemSensitivity(self):
        for widName in ['itemNameBox','itemBonusBox','itemDescriptionBox','itemEnabledButton']:
            wid = self[widName]
            wid.set_sensitive(self.activeItem is not None)
    def OnItemChange(self,item):
        if item is self.activeItem and item is not None:
            self['itemNameBox'].set_text(item.Name)
            self['itemBonusBox'].set_text(item.RelativeSaveString())
            self['itemEnabledButton'].set_active(not item.NoBonus)
            better_set_text(self['itemDescriptionBox'].get_buffer(),item.Description)
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
            self['rcItemMenu'].popup(
                None,None,None,event.button,event.time)
    def FromAddItem(self,*args):
        newItem = Character.Item(None,Names=['New Item'],Options=['Item'])
        self.char.AddVal(newItem)
        self.Update()
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
        self.Update()
    def FromActiveStatNameChange(self,widget):
        if self.activeStat is not None:
            self.activeStat.Name = widget.get_text()
        self.Update()
    def FromActiveStatCurrentChange(self,widget):
        if self.activeStat is not None:
            try:
                self.activeStat.Value = int(widget.get_text())
            except ValueError:
                pass
        self.Update()
    def FromActiveStatPotentialChange(self,widget):
        if self.activeStat is not None:
            try:
                self.activeStat.Max = int(widget.get_text())
            except ValueError:
                pass
        self.Update()
    def FromActiveStatDescriptionChange(self,widget):
        if self.activeStat is not None:
            text = widget.get_text(widget.get_start_iter(),widget.get_end_iter())
            self.activeStat.Description = text
        self.Update()
    def FromActiveStatLevellingChange(self,widget):
        if self.activeStat is not None:
            self.activeStat.Delta = int(widget.get_value())
        self.Update()
    def FromActiveSkillNameChange(self,widget):
        if self.activeSkill is not None:
            self.activeSkill.Name = self['skillNameBox'].get_text()
        self.Update()
    def FromActiveSkillRankChange(self,widget):
        if self.activeSkill is not None:
            try:
                self.activeSkill.Value = int(widget.get_text())
            except ValueError:
                pass
        self.Update()
    def FromActiveSkillDescriptionChange(self,widget):
        if self.activeSkill is not None:
            text = widget.get_text(widget.get_start_iter(),widget.get_end_iter())
            self.activeSkill.Description = text
        self.Update()
    def FromActiveItemNameChange(self,widget):
        if self.activeItem is not None:
            self.activeItem.Name = widget.get_text()
        self.Update()
    def FromActiveItemBonusChange(self,widget):
        if self.activeItem is not None:
            self.activeItem.ChangeBonuses(widget.get_text())
        self.Update()
    def FromActiveItemEnabledChange(self,widget):
        if self.activeItem is not None:
            self.activeItem.NoBonus = not widget.get_active()
        self.Update()
    def FromActiveItemDescriptionChange(self,widget):
        if self.activeItem is not None:
            self.activeItem.Description = widget.get_text(widget.get_start_iter(),
                                                          widget.get_end_iter())
        self.Update()
    def FromLevelUp(self,*args):
        self.char.ApplyLevelUp()
        self.ShowHideLevelling()
        self.Update()



def Run():
    gui = MainWindow()
    gui.Show()
    if len(sys.argv)>=2:
        gui.LoadFile(sys.argv[1])
    gtk.main()
