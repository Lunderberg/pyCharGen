from collections import defaultdict

"""
EventHandler calls each function registered to a particular key whenever the EventHandler is called.

'Stat Changed' is called when the value of a stat is changed.
'Skill Changed' is called when the value of a skill is changed.
'Resistance Changed' is called when the value of a resistance is changed.
'Value Added' is called when a value is added to the character.
"""

class EventHandler:
    def __init__(self):
        self.EventDict = defaultdict(list)
        self.Enabled = True
    def __call__(self, key, *args, **kwargs):
        if self.Enabled:
            for func in self.EventDict[key]:
                func(*args,**kwargs)
    def Register(self,key,func):
        self.EventDict[key].append(func)
    def Remove(self,key,func):
        try:
            self.EventDict[key].remove(func)
        except ValueError:
            pass

