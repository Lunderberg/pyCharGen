#!/usr/bin/env python

import unittest
import os.path as path

from backend import Parser,CulturePrototype

cultureFile = path.join(path.dirname(__file__),'TestCultures.txt')
charFile = path.join(path.dirname(__file__),'BigTestChar.txt')

class CultureTester(unittest.TestCase):
    def test_parsing_option(self):
        f = Parser.cultureOption.parseString
        self.assertEqual(f('Linguistics+1')[0],(['Linguistics'],1,False))
        self.assertEqual(f('Linguistics/*+1')[0],(['Linguistics',0],1,False))
        self.assertEqual(f('Linguistics/*+1r')[0],(['Linguistics',0],1,True))
        self.assertEqual(f('(Linguistics|Social)/*+1')[0],
                         ([['Linguistics','Social'],0],1,False))
        self.assertEqual(f('$PREV/*+1')[0],([1,0],1,False))
        self.assertEqual(f('$PREV1/*+1')[0],([1,0],1,False))
        self.assertEqual(f('$PREV2/*+1')[0],([2,0],1,False))
    def test_parsing_all(self):
        protos = Parser.cultureFile(cultureFile)
        self.assertEqual(protos[0].Name,'Cosmopolitan')
        self.assertEqual(protos[0].options[7],(['Survival','Region, Own'],1,True))
        self.assertEqual(protos[1].Name,'Rural')
        self.assertEqual(protos[1].options[8],(['Animal Handling',0],1,True))
    def test_culture_making(self):
        proto = Parser.cultureFile(cultureFile)[1]
        proto.char = Parser.characterFile(charFile)
        self.assertEqual(len(proto.Culture.ChildValues),6)
        proto.Select(1,0)
        proto.Select(2,0)
        proto.Select(3,0)
        proto.Select(13,0)
        culture = proto.Culture
        self.assertEqual(len(culture.ChildValues),10)


if __name__=='__main__':
    unittest.main()
