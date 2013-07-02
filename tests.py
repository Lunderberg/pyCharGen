#!/usr/bin/env python

import unittest
import os.path as path
import sys

import Character
import DiceParse
import TreeModelHelpers as TMH
from MainWindow import MainWindow


from DAG_tests import *

charfile = path.join(path.dirname(sys.argv[0]),'TestChar.txt')

class TestDiceParse(unittest.TestCase):
    def test_dice_parse(self):
        self.assertRaises(Exception,DiceParse.DiceParse,')')
        self.assertRaises(Exception,DiceParse.DiceParse,'(4+3))')
        self.assertRaises(Exception,DiceParse.DiceParse,'3**2')
        self.assertEqual(DiceParse.DiceParse("3+4").Roll(),7)
        self.assertEqual(DiceParse.DiceParse("12*5").Roll(),60)
        self.assertEqual(DiceParse.DiceParse("4d1").Roll(),4)
        self.assertEqual(DiceParse.DiceParse("10/(3+2)").Roll(),2)
        self.assertEqual(DiceParse.DiceParse("10*V").Roll(4),40)
        self.assertEqual(DiceParse.DiceParse("10^V").Roll(4),10000)
        self.assertEqual(DiceParse.DiceParse("50/20").Roll(4),2)
    def test_table(self):
        table = DiceParse.Table(path.join(path.dirname(sys.argv[0]),
                                          'tables','StatBonus.txt'))
        self.assertEqual(table(50),0)

class TestStatSkill(unittest.TestCase):
    def test_stat_bonus(self):
        testStat = Character.Stat(50)
        self.assertEqual(testStat.SelfBonus(),0)
        testStat.Value = 1
        self.assertEqual(testStat.SelfBonus(),-15)
        testStat.Value = 100
        self.assertEqual(testStat.SelfBonus(),15)
        testStat.Value = 100
        self.assertEqual(testStat.SelfBonus(),15)
        testStat.Value = 65
        self.assertEqual(testStat.SelfBonus(),2)
        testStat.Value = 29
        self.assertEqual(testStat.SelfBonus(),-4)
    def test_skill_bonus(self):
        testSkill = Character.Skill(0)
        self.assertEqual(testSkill.SelfBonus(),-25)
        testSkill.Value = 5
        self.assertEqual(testSkill.SelfBonus(),25)
        testSkill.Value = 15
        self.assertEqual(testSkill.SelfBonus(),65)
        testSkill.Value = 25
        self.assertEqual(testSkill.SelfBonus(),90)
        testSkill.Value = 35
        self.assertEqual(testSkill.SelfBonus(),105)
    def test_skill_delta(self):
        testSkill = Character.Skill(0)
        testSkill.Delta = 5
        self.assertEqual(testSkill.SelfBonus(),-25)
        self.assertEqual(testSkill.SelfBonus(levelled=True),25)
    def test_stat_minmax(self):
        testStat = Character.Stat(50)
        testStat.Min = 5
        self.assertEqual(testStat.Min,5)
        testStat.Max = 75
        self.assertEqual(testStat.Max,75)

class TestChar(unittest.TestCase):
    def test_char_building(self):
        char = Character.Character.Open(charfile)
        self.assertEqual(char['Agility'].Value,1)
        self.assertEqual(char['Ag'].Value,1)
        self.assertEqual(char['Constitution'].Value,100)
        self.assertEqual(char['Linguistics'].Value,0)
        self.assertEqual(char['Lore'].Bonus(),17)
        self.assertEqual(len(list(char.Stats)),10)
        self.assertEqual(len(list(char.Skills)),5)
        self.assertEqual(char.GetMisc('Name'),'Grognar')
        self.assertEqual(char.GetMisc('PlayerName'),'Grog')
        self.assertEqual(char.GetMisc('Profession'),'Fighter')
        self.assertEqual(char.GetMisc('Race'),'Troll')
        self.assertEqual(char.GetMisc('Level'),3)
        self.assertEqual(char.GetMisc('Experience'),12345)
    def test_linking(self):
        c = Character.Character()

        par1 = Character.Stat(100,Names=['name1'])
        c.AddVal(par1)
        par2 = Character.Skill(25,Names=['name2'])
        c.AddVal(par2)
        child = Character.Skill(1,Names=['child'],Parents=['name1','name2'])
        c.AddVal(child)

        pars = child.Parents
        self.assertIs(par1,pars[0])
        self.assertIs(par2,pars[1])
        self.assertEqual(len(pars),2)
        self.assertEqual(child.Bonus(),child.SelfBonus()+par1.SelfBonus()+par2.SelfBonus())

        item1 = Character.Item(None,Children=['child+5'])
        c.AddVal(item1)
        self.assertEqual(len(child.Parents),3)
        pars = child.Parents
        self.assertIs(par1,pars[0])
        self.assertIs(par2,pars[1])
        self.assertIs(item1,pars[2])

        self.assertEqual(child.Bonus(verbose=True),child.SelfBonus()+par1.SelfBonus()+par2.SelfBonus()+5)
        c.RemoveVal(par2)
        pars = child.Parents
        self.assertIs(par1,pars[0])
        self.assertIs(item1,pars[1])
        self.assertEqual(len(pars),2)
    def test_resistances(self):
        char = Character.Character.Open(charfile)
        self.assertEqual(char['Poison'].Bonus(),42)
        self.assertEqual(char['Disease'].Bonus(),42)
        self.assertEqual(char['Fear'].Bonus(),39)
        self.assertEqual(char['Channeling'].Bonus(),28)
        self.assertEqual(char['Essence'].Bonus(),32)
        self.assertEqual(char['Mentalism'].Bonus(),12)
    def test_weaponlist(self):
        char = Character.Character.Open(charfile)
        self.assertEqual(len(char.WeaponCostList),3)
        self.assertEqual(char.WeaponCostList[0],[1,3])
        self.assertEqual(char.WeaponCostList[1],[2,4])
        self.assertEqual(char.WeaponCostList[2],[5,7])

class TestStatSkillStores(unittest.TestCase):
    def setUp(self):
        self.char = Character.Character.Open(charfile)
    def test_statstore(self):
        store = TMH.StatListStore(self.char)
        for row,stat in zip(store,self.char.Stats):
            self.assertIs(row[TMH.StatListStore.col('obj')],stat)
            self.assertEqual(row[TMH.StatListStore.col('Name')],stat.Name)
            self.assertEqual(row[TMH.StatListStore.col('Temporary')],stat.Value)
            self.assertEqual(row[TMH.StatListStore.col('SelfBonus')],stat.SelfBonus())
            self.assertEqual(row[TMH.StatListStore.col('Bonus')],stat.Bonus())
        for stIter,stat in zip(store.IterAll,self.char.Stats):
            st,stName,stSB,stBon,stTemp = store.get(stIter,
                                                    TMH.StatListStore.col('obj'),TMH.StatListStore.col('Name'),
                                                    TMH.StatListStore.col('SelfBonus'),TMH.StatListStore.col('Bonus'),
                                                    TMH.StatListStore.col('Temporary'))
            self.assertIs(st,stat)
            self.assertEqual(stName,stat.Name)
            self.assertEqual(stSB,stat.SelfBonus())
            self.assertEqual(stBon,stat.Bonus())
            self.assertEqual(stTemp,stat.Value)
    def test_skillstore(self):
        store = TMH.SkillTreeStore(self.char)
        for skIter,skill in zip(store.IterAll,self.char.Skills):
            sk,skName,skSB,skBon,skRanks = store.get(skIter,
                                                     TMH.SkillTreeStore.col('obj'),TMH.SkillTreeStore.col('Name'),
                                                     TMH.SkillTreeStore.col('SelfBonus'),TMH.SkillTreeStore.col('Bonus'),
                                                     TMH.SkillTreeStore.col('Ranks'))
            self.assertIs(sk,skill)
            self.assertEqual(skName,skill.Name)
            self.assertEqual(skSB,skill.SelfBonus())
            self.assertEqual(skBon,skill.Bonus())
            self.assertEqual(skRanks,skill.Value)

class TestStringOut(unittest.TestCase):
    def setUp(self):
        self.char = Character.Character.Open(charfile)
    def test_value_strings(self):
        char = Character.Character()
        par1 = Character.Value(0,['L O N G  N A M E','short'])
        char.AddVal(par1)
        par2 = Character.Value(0,['SD','Self Discipline'])
        char.AddVal(par2)
        v = Character.Value(5,['test'])
        self.assertEqual(v.SaveString(),'test : 5')
        v.requestedParents = ['L O N G  N A M E','SD']
        char.AddVal(v)
        self.assertEqual(v.SaveString(),'test {short, SD} : 5')
        v.Options = ['NoBonus']
        v.Value = None
        self.assertEqual(v.SaveString(),'test {short, SD} [NoBonus]')
        v.Names = ['new Test','nT','TNT']
        self.assertEqual(v.SaveString(),'new Test (nT, TNT) {short, SD} [NoBonus]')
    def test_char_string(self):
        self.char.SaveString()

class TestValueParse(unittest.TestCase):
    def test_value_building(self):
        sk = Character.Value.FromLine(r'    Test Name (nick1,nick2)<2,4> {par1}[] [Skill]: 5 "Descript \"hi\""')
        self.assertEqual(type(sk),Character.Skill)
        self.assertEqual(sk.Name,'Test Name')
        self.assertEqual(sk.Names[1],'nick1')
        self.assertEqual(sk.Names[2],'nick2')
        self.assertEqual(sk.requestedParents[0],'par1')
        self.assertEqual(sk.Value,5)
        self.assertEqual(sk.Description,'Descript "hi"')
        self.assertEqual(sk.Costs[0],2)
        self.assertEqual(sk.Costs[1],4)
        self.assertEqual(sk.SaveString(),
                         r'Test Name (nick1, nick2) [Skill] <2,4> : 5 "Descript \"hi\""')
    def test_item_parse(self):
        descList = [r'ItemDescription(axe){Axe+1,SD-2}[Item]',
                    r'ItemDescription(axe){ Axe +1, SD-2}[Item]',
                    r'ItemDescription (axe){ Axe+1,SD- 2}[Item]',
                    r'ItemDescription(axe) {Axe + 1,  SD-2}[Item]']
        for description in descList:
            it = Character.Value.FromLine(description)
            self.assertEqual(type(it),Character.Item)
            self.assertEqual(it.Name,'ItemDescription')
            self.assertEqual(it.Names[1],'axe')
            self.assertEqual(it.requestedChildren[0],'Axe')
            self.assertEqual(it.requestedChildren[1],'SD')
            self.assertEqual(it.ChildValues[0][0],'Axe')
            self.assertEqual(it.ChildValues[0][1],1)
            self.assertEqual(it.ChildValues[1][0],'SD')
            self.assertEqual(it.ChildValues[1][1],-2)
            self.assertEqual(it.SaveString(),r'ItemDescription (axe) {Axe+1, SD-2} [Item]')
    def test_string_splitting(self):
        f = Character._split_by_special
        self.assertEqual(f('String with no special chars'),['String with no special chars'])
        self.assertEqual(f('Single: split'),['Single',':','split'])
        self.assertEqual(f('Escaped\: split'),['Escaped: split'])
        self.assertEqual(f('Commented# rest of line: {}'),['Commented'])
        self.assertEqual(f('Repeated specials {}:'),['Repeated specials','{','}',':'])
        self.assertEqual(f('Double slash \\\\'),['Double slash \\'])
        self.assertEqual(f('Triple slash \\\\\\'),['Triple slash \\\\'])

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.gui = MainWindow()
        self.char = Character.Character.Open(charfile)
    def test_load_misc(self):
        self.gui.LoadChar(self.char)
        self.assertEqual(self.gui.b.get_object('characterName').get_text(),'Grognar')
        self.assertEqual(self.gui.b.get_object('playerName').get_text(),'Grog')
        self.assertEqual(self.gui.b.get_object('profName').get_text(),'Fighter')
        self.assertEqual(self.gui.b.get_object('raceName').get_text(),'Troll')
        self.assertEqual(self.gui.b.get_object('charLevel').get_text(),'3')
        self.assertEqual(self.gui.b.get_object('cultureName').get_text(),'Hobbit')
        self.assertEqual(self.gui.b.get_object('experience').get_text(),'12345')
    def test_load_stats(self):
        self.gui.LoadChar(self.char)
        self.assertEqual(self.gui.b.get_object('statTable').get_property('n-columns'),5)
        self.assertEqual(self.gui.b.get_object('statTable').get_property('n-rows'),13)
        temp,bonus = self.gui.statWidgets['Constitution']
        self.assertEqual(temp.get_text(),'100')
        self.assertEqual(bonus.get_text(),'15')
        temp,bonus = self.gui.statWidgets['Memory']
        self.assertEqual(temp.get_text(),'50')
        self.assertEqual(bonus.get_text(),'0')
        temp,bonus = self.gui.statWidgets['Self Discipline']
        self.assertEqual(temp.get_text(),'97')
        self.assertEqual(bonus.get_text(),'12')
        for row in self.gui.statStore:
            if row[TMH.StatListStore.col('Name')]=='Agility':
                agRow = row
            elif row[TMH.StatListStore.col('Name')]=='Presence':
                prRow = row
        self.assertEqual(agRow[TMH.StatListStore.col('Temporary')],1)
        self.assertEqual(agRow[TMH.StatListStore.col('Bonus')],-15)
        self.assertEqual(prRow[TMH.StatListStore.col('Temporary')],50)
        self.assertEqual(prRow[TMH.StatListStore.col('Bonus')],0)
        agRow[TMH.StatListStore.col('obj')].Value = 100
        self.gui.Update()
        self.assertEqual(agRow[TMH.StatListStore.col('Bonus')],15)
    def test_load_skills(self):
        self.gui.LoadChar(self.char)
        for skIter in self.gui.skillStore.IterAll:
            skill,ranks,bonus = self.gui.skillStore.get(skIter,
                                                        TMH.SkillTreeStore.col('obj'),
                                                        TMH.SkillTreeStore.col('Ranks'),
                                                        TMH.SkillTreeStore.col('Bonus'))
            if skill.Name=='Elvish':
                self.assertEqual(ranks,1)
                self.assertEqual(bonus,9020)
                skill.Value = 15
                self.gui.Update()
                skill,ranks,bonus = self.gui.skillStore.get(skIter,
                                                            TMH.SkillTreeStore.col('obj'),
                                                            TMH.SkillTreeStore.col('Ranks'),
                                                            TMH.SkillTreeStore.col('Bonus'))
                self.assertEqual(ranks,15)
                self.assertEqual(bonus,9080)
    def test_load_items(self):
        self.gui.LoadChar(self.char)
        bookIter,earIter = list(self.gui.itemStore.IterAll)
        book = self.gui.itemStore.get(bookIter,TMH.ItemListStore.col('obj'))[0]
        ear = self.gui.itemStore.get(earIter,TMH.ItemListStore.col('obj'))[0]
        self.assertEqual(self.gui.itemStore.get(bookIter,TMH.ItemListStore.col('Name'))[0],'Research Book')
        book.Name = 'Researchy Awesome Book'
        self.gui.Update()
        self.assertEqual(self.gui.itemStore.get(bookIter,TMH.ItemListStore.col('Name'))[0],'Researchy Awesome Book')
        ear.Description = 'Maybe a bit transparent'
        self.gui.Update()
        self.assertEqual(self.gui.itemStore.get(earIter,TMH.ItemListStore.col('Description'))[0],
                         'Maybe a bit transparent')

if __name__=='__main__':
    unittest.main()
