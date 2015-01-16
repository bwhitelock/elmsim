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
        self.pack(fill=BOTH,expand=True)
        twoFrame1=Frame(self)
        twoFrame1.pack(fill=BOTH,expand=True)
        button = Tkinter.Button(twoFrame1,text=u"Stop Device",
                                command=self.OnButtonClick)
        button.pack(expand=True)
        button2 = Tkinter.Button(twoFrame1,text=u"Start Device",
                                command=self.OnButton2Click)
        button2.pack(side=LEFT,expand=True)

        twoFrame2=Frame(self)
        twoFrame2.pack(fill=BOTH,expand=True)
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(twoFrame2,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        self.labelVariable.set(u"Hello !")
        label.pack(fill=X,expand=True)
        twoFrame3=Frame(self)
        twoFrame3.pack(fill=BOTH,expand=True)
        label2 = Tkinter.Label(twoFrame3,text='testing',
                              anchor="w",fg="white",bg="blue")
        label2.pack(fill=X,expand=True)
        self.update()

    def OnButtonClick(self):
        print "You clicked button1 !"
        self.device.stop()

    def OnButton2Click(self):
        print "You clicked button2 !"
        self.device.listen()
