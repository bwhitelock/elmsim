#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent,device):
        Tkinter.Tk.__init__(self,parent)
        self.device=device
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        currentColumn=0
        currentRow=0
        speedLabel = Tkinter.Label(self, text='Speed', fg="white",bg="blue")
        speedLabel.grid(column=0,row=currentRow,sticky='EW')
        rpmLabel = Tkinter.Label(self, text='RPM', fg="white",bg="blue")
        rpmLabel.grid(column=1,row=currentRow,sticky='EW')
        tempLabel = Tkinter.Label(self, text='Temp', fg="white",bg="blue")
        tempLabel.grid(column=2,row=currentRow,sticky='EW')

        currentRow=currentRow+1
        self.speedValue=0
        self.speedScale = Tkinter.Scale(from_=0,to=200, orient=Tkinter.VERTICAL,
            command=self.OnSpeedChange)
        self.speedScale.grid(column=0,row=currentRow,sticky='NS')
        self.speedScale.bind("<ButtonRelease-1>", self.speedChanged)
        self.rpmValue=0
        self.rpmScale = Tkinter.Scale(from_=0,to=6000, orient=Tkinter.VERTICAL,
            resolution=100, command=self.OnRPMChange)
        self.rpmScale.grid(column=1,row=currentRow,sticky='NS')
        self.rpmScale.bind("<ButtonRelease-1>", self.rpmChanged)
        self.tempValue=0
        self.tempScale = Tkinter.Scale(from_=0,to=200, orient=Tkinter.VERTICAL,
            command=self.OnTempChange)
        self.tempScale.grid(column=2,row=currentRow,sticky='NS')
        self.tempScale.bind("<ButtonRelease-1>", self.tempChanged)

        currentRow=currentRow+1
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=1,row=currentRow,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here.")

        button = Tkinter.Button(self,text=u"Click me !",
                                command=self.OnButtonClick)
        button.grid(column=2,row=currentRow)

        currentRow=currentRow+1
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=currentRow,columnspan=3,sticky='EW')
        self.labelVariable.set(u"Hello !")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get()+" (You clicked the button)")
        print "You clicked the button !"
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        self.device.stop()

    def OnPressEnter(self,event):
        self.labelVariable.set(self.entryVariable.get()+" (You pressed ENTER)" )
        print "You pressed enter !"
        source = ['entry',self.entryVariable.get()]
        self.device.putData(source)
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnSpeedChange(self,value):
        #print "speed set to:",value
        self.speedValue=value

    def speedChanged(self,event):
        print "speed set to:",self.speedValue

    def OnRPMChange(self,value):
        self.rpmValue=value

    def rpmChanged(self,event):
        print "rpm set to:",self.rpmValue

    def OnTempChange(self,value):
        self.tempValue=value

    def tempChanged(self,event):
        print "temp set to:",self.tempValue

#app = simpleapp_tk(None)
#app.title('ELM327 Simulator')
#print "mainloop"
#app.mainloop()
#print "leaving tk app"
#app.device.stop()
#app.device.join(5)
#device.stop()
#device.join(5)
#if app.device.is_alive():
    #print "terminating elm device"
    #app.device.terminate()
#if device.is_alive():
    #print "terminating elm device"
    #device.terminate()
