#from multiprocessing import Process, Queue
import multiprocessing, Queue
from threading import Thread
#import pty
import os, sys, select
import time
from atType1 import atType1

class openPort(Thread):
    def __init__ (self,parent,queue):
        Thread.__init__(self)
        self.parent=parent
        self.queue=queue
        self.exit = multiprocessing.Event()
        (self.master, slave )= os.openpty()
        self.s_name = os.ttyname(slave)
        os.close(slave)
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
                dataSource = dataSource.upper()
                dataSource = dataSource.replace(' ','')
                if dataSource[:2] == 'AT':
                    print "at command"
                    #response=self.atcmd(dataSource)
                    if atType1.get(dataSource):
                        print "using dict call",atType1[dataSource]
                        response=atType1[dataSource]()
                        #response=ResetAll()
                        print "dict response",response
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
