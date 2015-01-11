#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter
from ttk import *
from testTab1 import testTab1
from testTab2 import testTab2
from engineTab import engineTab
import Queue

class simpleapp_tk(Tkinter.Tk):
    #def __init__(self,parent,device,queue):
    def __init__(self,parent,device,queue):
        Tkinter.Tk.__init__(self,parent)
        self.device=device
        self.parent = parent
        self.returnQueue=queue
        self.initialize()

    def initialize(self):
        master = Frame(self.parent, name='master')
        master.pack(fill=BOTH,expand=True)
        self.notebook = Notebook(master, name='nb')
        self.notebook.pack(fill=BOTH,expand=True)

        self.engineTab = engineTab(self.notebook, self.device, name='engineTab')
        self.notebook.add(self.engineTab, text="Engine")

        self.testTab1 = testTab1(self.notebook, self.device, name='Tab 1')
        self.notebook.add(self.testTab1, text="Tab 1")

        self.testTab2 = testTab2(self.notebook, self.device, name='secondTab')
        self.notebook.add(self.testTab2, text="Tab 2")

        self.resizable(True,True)
        self.after(500,self.doCommand)
        self.update()

    def doCommand(self):
        try:
            content=self.returnQueue.get_nowait()
            print "return contents:",content
        except Queue.Empty:
            pass
        #print "running do command"
        self.after(500,self.doCommand)

