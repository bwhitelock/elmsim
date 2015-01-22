#from multiprocessing import Process, Queue
import multiprocessing, Queue
from threading import Thread
#import pty
import os, sys, select
import time
#from atCommands import atCommands
#from includes.modeConsts import modeConsts
#from includes.mainPIDs import mainPIDs
#from engineControlUnits.ecu import ecu


class openPort(Thread):
    def __init__ (self,parent,queue):
    #def __init__ (self,parent,queue,ecu):
        Thread.__init__(self)
        self.parent=parent
        self.queue=queue
        self.exit = multiprocessing.Event()
        (self.master, slave )= os.openpty()
        self.s_name = os.ttyname(slave)
        #os.close(slave)
        print "serial name:", self.s_name
        self.echo = True
        #self.ecu = ecu()
        #self.ecu = ecu


    def run(self):
        print "starting openPort"
        source = ['port',self.s_name]
        self.parent.putData(source)
        dataSource = ""
        lastLine = ""
        while not self.exit.is_set():
            print "openPort loop"
            try:
                data = ''
                cmd = ''
                dataSource = ''
                response = ''
                repeatLast=False
                while not ((data == '\r') or (data == '\n')):
                    data=os.read(self.master,1000)
                    if data == '\r':
                        if ((dataSource == '') and not(lastLine == '')):
                            dataSource=''.join(lastLine)
                            repeatLast=True
                    else:
                        dataSource += data
                    if self.echo:
                        os.write(self.master,data)

                if repeatLast == False:
                    lastLine=''.join(dataSource)
                else:
                    print "repeatLast",repeatLast
                    if self.echo:
                        os.write(self.master,'\r')
                        os.write(self.master,'\n')
                        os.write(self.master,dataSource)
                        os.write(self.master,'\r')
                if len(dataSource) > 1: #There are no commands less than 2
                    dataSource = dataSource.upper()
                    dataSource = dataSource.replace(' ','')
                    response = '?'
                    if dataSource[:2] == 'AT':
                        print "at command loaded"
                        source = ['atCmd',dataSource]
                    else:
                        print "pid command loaded"
                        source = ['pidCmd',dataSource]
                    #response=self.processPortData(dataSource)
                    print "putting portData on queue"
                    self.parent.putData(source)
                    response = self.queue.get()
                    print "elmport response from elmDevice is",response

                if not response == '':
                    if self.echo:
                        os.write(self.master,'\n')
                    os.write(self.master,response)
                    if self.echo:
                        os.write(self.master,'\r')
                if self.echo:
                    os.write(self.master,'\n')
                os.write(self.master,'>')
            except:
                time.sleep(1)

    def stop(self):
        print "stopping openPort"
        self.exit.set()
        
#    def processPortData(self,data):
#        data = data.upper()
#        data = data.replace(' ','')
#        response = '?'
#        #if len(data) == 2:
#            #print "mode 3 or mode 4 request"
#            #return "OK"
#        if data[:2] == 'AT':
#            print "at command"
#            if atCommands.get(data[:6]):
#                print "using dict call",atCommands[data[:6]]
#                response=atCommands[data[:6]](self)
#                print "dict response",response
#            elif atCommands.get(data[:5]):
#                print "using dict call",atCommands[data[:5]]
#                response=atCommands[data[:5]](self)
#                print "dict response",response
#            elif atCommands.get(data[:4]):
#                print "using dict call",atCommands[data[:4]]
#                response=atCommands[data[:4]](self)
#                print "dict response",response
#            elif atCommands.get(data[:3]):
#                print "using dict call",atCommands[data[:3]]
#                response=atCommands[data[:3]](self)
#                print "dict response",response
#            elif atCommands.get(data):
#                print "using dict call",atCommands[data]
#                response=atCommands[data](self)
#                print "dict response",response
#        else:
#            print "getting response from ecu"
#            #print "test",self.ecu.myTest()
#            #response = self.ecu.getResponseData(data)
#            print "ecu speed",self.ecu.speed
#            print "ecu rpm",self.ecu.rpm
#            print "ecu rpm",self.ecu.getRPM()
#            #response = self.ecu.response
#            #response = self.ecu.getResponseData(data,ecuData)
#        #elif data[:2] == '01': #Mode 01
#            #pid = data[2:4]
#            #print "pid",pid
#            #if not (mainPIDs.get(pid) == None):
#                #consts = modeConsts()
#                #print "consts",consts
#                #pidMode = 1
#                #print "pidMode",pidMode
#                #minVal = mainPIDs[pid][consts.minValue]
#                #print "minVal",minVal
#                #maxVal = mainPIDs[pid][consts.maxValue]
#                #print "maxVal",maxVal
#                #response=mainPIDs[pid][consts.funcCall](self,pidMode,minVal,maxVal,data)
#        #elif data[:2] == '02': #Mode 02
#            #pid = data[2:4]
#            #print "pid",pid
#            #if not (mainPIDs.get(pid) == None):
#                #consts = modeConsts()
#                #print "consts",consts
#                #pidMode = 2
#                #print "pidMode",pidMode
#                #minVal = mainPIDs[pid][consts.minValue]
#                #print "minVal",minVal
#                #maxVal = mainPIDs[pid][consts.maxValue]
#                #print "maxVal",maxVal
#                #response=mainPIDs[pid][consts.funcCall](self,pidMode,minVal,maxVal,data)
#        #elif data[:2] == '05': #Mode 05
#            #response='OK'
#        #elif data[:2] == '06': #Mode 06
#            #response='OK'
#        #elif data[:2] == '07': #Mode 07
#            #response='OK'
#        #elif data[:2] == '08': #Mode 08
#            #response='OK'
#        #elif data[:2] == '09': #Mode 09
#            #response='OK'
#        #elif data[:2] == '0A': #Mode 0A
#            #response='OK'
#
#        return response
