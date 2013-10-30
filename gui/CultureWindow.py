#!/usr/bin/env python

import gtk

class CultureWindow(object):
    def __init__(self,cultureprototype,callback):
        self.callback = callback
        self.cultureprototype = cultureprototype
        self.window = gtk.Window()
        self.window.connect('delete-event',self.Done)
        self.table = gtk.Table()
        self.window.add(self.table)
        self.boxes = []
        for i in range(len(self.cultureprototype)):
            box = gtk.combo_box_new_text()
            self.table.attach(box,0,1,i,i+1,xpadding=10*self.cultureprototype.Depth(i))
            box.connect('changed',self.OnBoxSelect,i)
            self.boxes.append(box)
            self.FillBox(i)
            bonus,ranks = self.cultureprototype.Bonus(i)
            self.table.attach(gtk.Label('{0:+d}'.format(bonus) + (' ranks' if ranks else '')), 1,2,i,i+1)
        doneButton = gtk.Button('Done')
        doneButton.connect('clicked',self.Done)
        self.table.attach(doneButton,1,2,len(self.cultureprototype),len(self.cultureprototype)+1)
    def Show(self):
        self.window.show_all()
    def Done(self,*args):
        self.window.destroy()
        self.callback(self)
    def OnBoxSelect(self,box,i):
        to_update = self.cultureprototype.Select(i,box.get_active())
        for updating in to_update:
            self.FillBox(updating)
    def FillBox(self,i):
        box = self.boxes[i]
        box.get_model().clear()
        opts = self.cultureprototype.Options(i)
        for sk in opts:
            box.append_text(sk.Name)
        if len(opts)==1:
            box.set_active(0)
        box.set_sensitive(len(opts)>1)
    @property
    def Culture(self):
        return self.cultureprototype.Culture
