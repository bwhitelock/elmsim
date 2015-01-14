#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter
from ttk import *

class engineTab(Frame):
    def __init__(self, master=None, device=None, name=None):
        Frame.__init__(self, master)
        self.device=device
        self.name=name
        currentRow=0
        #self.grid(sticky=N+S+E+W)
        self.pack(fill=BOTH)
        speedFrame=Frame(self)
        speedFrame.pack(fill=BOTH,side=LEFT,expand=True)
        speedLabel = Tkinter.Label(speedFrame, text='Speed', fg="white",bg="blue")
        #speedLabel.grid(column=0,row=0,sticky=W+E+N+S)
        speedLabel.pack(fill=X,expand=True)

        currentRow=currentRow+1
        self.speedValue=0
        self.speedScale = Tkinter.Scale(speedFrame,from_=0,to=200, orient=Tkinter.VERTICAL,
            command=self.OnSpeedChange)
        #self.speedScale.grid(column=0,row=1,sticky=W+E+N+S)
        self.speedScale.pack(fill=Y,expand=True)
        self.speedScale.bind("<ButtonRelease-1>", self.speedChanged)

        rpmFrame=Frame(self)
        rpmFrame.pack(fill=BOTH,side=LEFT,expand=True)
        rpmLabel = Tkinter.Label(rpmFrame, text='RPM', fg="white",bg="blue")
        #rpmLabel.grid(column=1,row=0,sticky=W+E+N+S)
        rpmLabel.pack(fill=X,expand=True)
        self.rpmValue=0
        self.rpmScale = Tkinter.Scale(rpmFrame,from_=0,to=6000, orient=Tkinter.VERTICAL,
            resolution=100, command=self.OnRPMChange)
        #self.rpmScale.grid(column=1,row=1,sticky=W+E+N+S)
        self.rpmScale.pack(fill=Y,expand=True)
        self.rpmScale.bind("<ButtonRelease-1>", self.rpmChanged)

        tempFrame=Frame(self)
        tempFrame.pack(fill=BOTH,side=LEFT,expand=True)
        tempLabel = Tkinter.Label(tempFrame, text='Temp', fg="white",bg="blue")
        #tempLabel.grid(column=2,row=0,sticky=W+E+N+S)
        tempLabel.pack(fill=X,expand=True)
        self.tempValue=0
        self.tempScale = Tkinter.Scale(tempFrame,from_=0,to=200, orient=Tkinter.VERTICAL,
            command=self.OnTempChange)
        #self.tempScale.grid(column=2,row=1,sticky=W+E+N+S)
        self.tempScale.pack(fill=Y,expand=True)
        self.tempScale.bind("<ButtonRelease-1>", self.tempChanged)

    def OnSpeedChange(self,value):
        #print "speed set to:",value
        self.speedValue=value

    def speedChanged(self,event):
        print "speed set to:",self.speedValue
        source = ['speed',self.speedValue]
        self.device.putData(source)

    def OnRPMChange(self,value):
        self.rpmValue=value

    def rpmChanged(self,event):
        print "rpm set to:",self.rpmValue
        source = ['rpm',self.rpmValue]
        self.device.putData(source)

    def OnTempChange(self,value):
        self.tempValue=value

    def tempChanged(self,event):
        print "temp set to:",self.tempValue
        source = ['temp',self.tempValue]
        self.device.putData(source)
