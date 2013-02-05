#!/usr/bin/env python

import unittest
import os.path as path

import Character
import DiceParse
from TreeModelHelpers import StatStore,SkillStore,AddTextColumn,AddCheckboxColumn

charfile = path.join(path.dirname(__file__),'TestChar.txt')

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
        table = DiceParse.Table(path.join(path.dirname(__file__),
                                          'tables','StatBonus.txt'))
        self.assertEqual(table(50),0)

class TestStatSkill(unittest.TestCase):
    def test_stat_bonus(self):
        testStat = Character.Stat(50)
        self.assertEqual(testStat.SelfBonus,0)
        testStat.Value = 1
        self.assertEqual(testStat.SelfBonus,-15)
        testStat.Value = 100
        self.assertEqual(testStat.SelfBonus,15)
        testStat.Value = 100
        self.assertEqual(testStat.SelfBonus,15)
        testStat.Value = 65
        self.assertEqual(testStat.SelfBonus,2)
        testStat.Value = 29
        self.assertEqual(testStat.SelfBonus,-4)
    def test_skill_bonus(self):
        testSkill = Character.Skill(0)
        self.assertEqual(testSkill.SelfBonus,-25)
        testSkill.Value = 5
        self.assertEqual(testSkill.SelfBonus,25)
        testSkill.Value = 15
        self.assertEqual(testSkill.SelfBonus,65)
        testSkill.Value = 25
        self.assertEqual(testSkill.SelfBonus,90)
        testSkill.Value = 35
        self.assertEqual(testSkill.SelfBonus,105)
    def test_parentage(self):
        par1 = Character.Stat(100)
        par2 = Character.Skill(25)
        child = Character.Skill(1,Parents=[par1,par2])
        self.assertEqual(child.Bonus,child.SelfBonus+par1.SelfBonus+par2.SelfBonus)

class TestChar(unittest.TestCase):
    def test_char_building(self):
        char = Character.Character.Open(charfile)
        self.assertEqual(char['Agility'].Value,1)
        self.assertEqual(char['Ag'].Value,1)
        self.assertEqual(char['Constitution'].Value,100)
        self.assertEqual(char['Linguistics'].Value,0)
        self.assertEqual(char['Lore'].Bonus,15)
        self.assertEqual(len(list(char.Stats)),10)
        self.assertEqual(len(list(char.Skills)),5)
        self.assertEqual(char.Name,'Grognar')
        self.assertEqual(char.PlayerName,'Grog')
        self.assertEqual(char.Profession,'Fighter')
        self.assertEqual(char.Race,'Troll')
        self.assertEqual(char.Level,3)
        self.assertEqual(char.Experience,12345)
    def test_resistances(self):
        char = Character.Character.Open(charfile)
        self.assertEqual(char['Poison'].Bonus,42)
        self.assertEqual(char['Disease'].Bonus,42)
        self.assertEqual(char['Fear'].Bonus,39)
        self.assertEqual(char['Channeling'].Bonus,28)
        self.assertEqual(char['Essence'].Bonus,32)
        self.assertEqual(char['Mentalism'].Bonus,12)

class TestStatSkillStores(unittest.TestCase):
    def setUp(self):
        self.char = Character.Character.Open(charfile)
    def test_statstore(self):
        store = StatStore(self.char)
        for row,stat in zip(store,self.char.Stats):
            self.assertIs(row[StatStore.col('Stat')],stat)
            self.assertEqual(row[StatStore.col('Name')],stat.Name)
            self.assertEqual(row[StatStore.col('Temporary')],stat.Value)
            self.assertEqual(row[StatStore.col('SelfBonus')],stat.SelfBonus)
            self.assertEqual(row[StatStore.col('Bonus')],stat.Bonus)
        for stIter,stat in zip(store.IterAll,self.char.Stats):
            st,stName,stSB,stBon,stTemp = store.get(stIter,
                                                    StatStore.col('Stat'),StatStore.col('Name'),
                                                    StatStore.col('SelfBonus'),StatStore.col('Bonus'),
                                                    StatStore.col('Temporary'))
            self.assertIs(st,stat)
            self.assertEqual(stName,stat.Name)
            self.assertEqual(stSB,stat.SelfBonus)
            self.assertEqual(stBon,stat.Bonus)
            self.assertEqual(stTemp,stat.Value)
    def test_skillstore(self):
        store = SkillStore(self.char)
        for skIter,skill in zip(store.IterAll,self.char.Skills):
            sk,skName,skSB,skBon,skRanks = store.get(skIter,
                                                     SkillStore.col('Skill'),SkillStore.col('Name'),
                                                     SkillStore.col('SelfBonus'),SkillStore.col('Bonus'),
                                                     SkillStore.col('Ranks'))
            self.assertIs(sk,skill)
            self.assertEqual(skName,skill.Name)
            self.assertEqual(skSB,skill.SelfBonus)
            self.assertEqual(skBon,skill.Bonus)
            self.assertEqual(skRanks,skill.Value)

class TestStringOut(unittest.TestCase):
    def setUp(self):
        self.char = Character.Character.Open(charfile)
    def test_value_strings(self):
        par1 = Character.Value(0,['L O N G  N A M E','short'])
        par2 = Character.Value(0,['SD','Self Discipline'])
        v = Character.Value(5,['test'])
        self.assertEqual(v.SaveString(),'test: 5')
        v.Parents = [par1,par2]
        self.assertEqual(v.SaveString(),'test {short, SD}: 5')
        v.Options = ['NoBonus']
        v.Value = None
        self.assertEqual(v.SaveString(),'test {short, SD} [NoBonus]')
        v.Names = ['new Test','nT','TNT']
        self.assertEqual(v.SaveString(),'new Test (nT, TNT) {short, SD} [NoBonus]')
    def test_char_string(self):
        self.char.SaveString()

if __name__=='__main__':
    unittest.main()
