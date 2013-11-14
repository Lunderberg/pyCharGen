#!/usr/bin/env python

class Profession(object):
    """
    Holds the information relevant for a profession.
    Has self.Name, a string with the name of the profession,
      and self.Costs, a list of (SkillName,CostList) tuples.
    """
    def __init__(self,Name):
        self.Name = Name
        self.Costs = []
    def AddCost(self,Name,Costs):
        self.Costs.append((Name,Costs))
