#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter
from ttk import *

class testTab2(Frame):
    def __init__(self, master=None, device=None, name=None):
        Frame.__init__(self, master)
        self.device=device
        self.name=name
        #self.grid(sticky=N+W+E+S)
        self.pack(fill=BOTH,expand=True)
        twoFrame1=Frame(self)
        twoFrame1.pack(fill=BOTH,expand=True)
        button = Tkinter.Button(twoFrame1,text=u"Click me !",
                                command=self.OnButtonClick)
        #button.grid(column=0,row=0)
        button.pack(expand=True)

        twoFrame2=Frame(self)
        twoFrame2.pack(fill=BOTH,expand=True)
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(twoFrame2,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        self.labelVariable.set(u"Hello !")
        #label.grid(column=0,row=2)
        label.pack(fill=X,expand=True)
        twoFrame3=Frame(self)
        twoFrame3.pack(fill=BOTH,expand=True)
        label2 = Tkinter.Label(twoFrame3,text='testing',
                              anchor="w",fg="white",bg="blue")
        label2.pack(fill=X,expand=True)
        #self.columnconfigure(0,weight=1)
        self.update()

    def OnButtonClick(self):
        #self.labelVariable.set(self.entryVariable.get()+" (You clicked the button)")
        print "You clicked the button !"
        #self.entry.focus_set()
        #self.entry.selection_range(0, Tkinter.END)
        #self.firstTab.entry.focus_set()
        #self.firstTab.entry.selection_range(0, Tkinter.END)
        self.device.stop()
