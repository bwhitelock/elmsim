#from multiprocessing import Process, Queue
import multiprocessing, Queue
from threading import Thread
#import pty
import os, sys, select
import time
#from atType1 import atType1
#from atType2 import atType2
#from atType3 import atType3
#from atType4 import atType4
from includes.atCommands import atCommands
from includes.modeConsts import modeConsts
from includes.mainPIDs import mainPIDs


class openPort(Thread):
    def __init__ (self,parent,queue):
        Thread.__init__(self)
        self.parent=parent
        self.queue=queue
        self.exit = multiprocessing.Event()
        (self.master, slave )= os.openpty()
        self.s_name = os.ttyname(slave)
        #os.close(slave)
        print "serial name:", self.s_name
        self.echo = True


    def run(self):
        print "starting openPort"
        source = ['port',self.s_name]
        self.parent.putData(source)
        dataSource = ""
        lastLine = ""
        #ser.echo(False)
        #while True:
        #os.write(self.master,'>')
        #os.write(self.master,'ELM327 v2.0')
        while not self.exit.is_set():
            #time.sleep(0.25)
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
                        #print "data :",data
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
                    response=self.processPortData(dataSource)
                    #dataSource = dataSource.upper()
                    #print "dataSource upper",dataSource
                    #dataSource = dataSource.replace(' ','')
                    #if dataSource[:2] == 'AT':
                        #print "at command"
                        ##response=self.atcmd(dataSource)
                        #if atType1.get(dataSource):
                            #print "using dict call",atType1[dataSource]
                            #response=atType1[dataSource]()
                            ##response=ResetAll()
                            #print "dict response",response
                    #elif dataSource[:2] == '01': #Mode 1
                        #response='FFFFFFFF'
                    #elif dataSource[:2] == '02': #Mode 2
                        #response='FFFFFFFF'
                        ##print "using dict call",mode1[dataSource[2:3]]

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
        
    def atcmd(self,data):
        source = ['cmd','reset']
        self.parent.putData(source)
        print "run at command on data:",data
        if data == 'ATZ':
            result=''
        else:
            result='?'
        return result

    def processPortData(self,data):
        data = data.upper()
        data = data.replace(' ','')
        response = '?'
        if len(data) == 2:
            print "mode 3 or mode 4 request"
            return "OK"
        if data[:2] == 'AT':
            print "at command"
            #if atType1.get(data): #check for basic commands first
                #print "using dict call",atType1[data]
                #response=atType1[data](self)
                #print "dict response",response
            #elif atType2.get(data[:4]): #check for basic commands first
                #print "using dict call",atType2[data[:4]]
                #response=atType2[data[:4]](self)
                #print "dict response",response
            #elif atType3.get(data[:5]): #check for basic commands first
                #print "using dict call",atType3[data[:5]]
                #response=atType3[data[:5]](self)
                #print "dict response",response
            #elif atType4.get(data[:6]): #check for basic commands first
                #print "using dict call",atType4[data[:6]]
                #response=atType4[data[:6]](self)
                #print "dict response",response
            if atCommands.get(data[:6]):
                print "using dict call",atCommands[data[:6]]
                response=atCommands[data[:6]](self)
                print "dict response",response
            elif atCommands.get(data[:5]):
                print "using dict call",atCommands[data[:5]]
                response=atCommands[data[:5]](self)
                print "dict response",response
            elif atCommands.get(data[:4]):
                print "using dict call",atCommands[data[:4]]
                response=atCommands[data[:4]](self)
                print "dict response",response
            elif atCommands.get(data[:3]):
                print "using dict call",atCommands[data[:3]]
                response=atCommands[data[:3]](self)
                print "dict response",response
            elif atCommands.get(data):
                print "using dict call",atCommands[data]
                response=atCommands[data](self)
                print "dict response",response
        elif data[:2] == '01': #Mode 01
            #response='FFFFFFFF'
            pid = data[2:4]
            print "pid",pid
            if not (mainPIDs.get(pid) == None):
                consts = modeConsts()
                print "consts",consts
                numBytes = mainPIDs[pid][consts.numBytes]
                print "numBytes",numBytes
                minVal = mainPIDs[pid][consts.minValue]
                print "minVal",minVal
                maxVal = mainPIDs[pid][consts.maxValue]
                print "maxVal",maxVal
                response=mainPIDs[pid][consts.funcCall](self,numBytes,minVal,maxVal,data[5:])
        elif data[:2] == '02': #Mode 02
            response='FFFFFFFF'
        elif data[:2] == '05': #Mode 05
            response='OK'
        elif data[:2] == '06': #Mode 06
            response='OK'
        elif data[:2] == '07': #Mode 07
            response='OK'
        elif data[:2] == '08': #Mode 08
            response='OK'
        elif data[:2] == '09': #Mode 09
            response='OK'
        elif data[:2] == '0A': #Mode 0A
            response='OK'

        return response
