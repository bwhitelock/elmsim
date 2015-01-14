#from multiprocessing import Process, Queue
import multiprocessing, Queue
from threading import Thread
#import pty
import os, sys, select
import time

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
        while not self.exit.is_set():
            #time.sleep(0.25)
            print "openPort loop"
            try:
                data = ''
                cmd = ''
                dataSource = ''
                repeatLast=False
                while not ((data == '\r') or (data == '\n')):
                    data=os.read(self.master,1000)
                    if data == '\r':
                        print "cariage return"
                        if ((dataSource == '') and not(lastLine == '')):
                            dataSource=''.join(lastLine)
                            repeatLast=True
                    elif data == '\n':
                        print "line feed"
                    #elif ((data.upper() == 'T') and (dataSource.upper() == 'A')):
                        #cmd = 'AT'
                        #dataSource = ''
                        #print "T data:",data
                    else:
                        print "data :",data
                        dataSource += data
                    #dataSource += data
                    #if self.echo and (repeatLast == False):
                    if self.echo:
                        os.write(self.master,data)
                if repeatLast == False:
                    lastLine=''.join(dataSource)
                else:
                    print "repeatLast",repeatLast
                    if self.echo:
                        #os.write(self.master,'\n')
                        #os.write(self.master,'>')
                        os.write(self.master,dataSource)
                        os.write(self.master,'\r')
                print "lastLine",lastLine
                dataSource = dataSource.upper()
                dataSource = dataSource.replace(' ','')
                print "dataSource:",dataSource
                #if dataSource[:2].upper() == 'AT':
                if dataSource[:2] == 'AT':
                    self.atcmd(dataSource)
                #data=os.read(master)
                os.write(self.master,'\n')
                os.write(self.master,'>')
            except:
                time.sleep(0.25)
                #pass
                #print "read failed"

            #print "received data is:\n",dataSource

    def stop(self):
        print "stopping openPort"
        self.exit.set()
        
    def atcmd(self,data):
        source = ['cmd','reset']
        self.parent.putData(source)
        print "run at command on data:",data
