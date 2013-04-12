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
        self.Call_Immediately = False
        self.Prune_Redundant = True
        self._uncalled = []
    def __call__(self, key, *args, **kwargs):
        if self.Enabled:
            for func in self.EventDict[key]:
                if self.Call_Immediately:
                    func(*args,**kwargs)
                else:
                    self._uncalled.append( (func,args,kwargs) )
    def Register(self,key,func):
        self.EventDict[key].append(func)
    def Remove(self,key,func):
        try:
            self.EventDict[key].remove(func)
        except ValueError:
            pass
    def Execute(self):
        if self.Prune_Redundant:
            toCall = []
            for i in self._uncalled:
                if all(i!=j for j in toCall):
                    toCall.append(i)
        else:
            toCall = self._uncalled
        for func,args,kwargs in toCall:
            func(*args,**kwargs)
        self._uncalled = []
