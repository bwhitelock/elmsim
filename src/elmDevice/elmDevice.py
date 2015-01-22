#from multiprocessing import Process, Queue
import multiprocessing, Queue
from threading import Thread
from elmport import openPort
#import pty
import os
import time
from ecu.ecu import ecu
from ecu.ecuData import ecuData
from atCommands import atCommands

class elmDevice (multiprocessing.Process):
    def __init__(self,queue):
        multiprocessing.Process.__init__(self)
        print "in elmDevice"
        self.deviceQueue = multiprocessing.Queue(10)
        self.portQueue = multiprocessing.Queue(1)
        self.exit = multiprocessing.Event()
        self.listening = multiprocessing.Event()
        self.daemon=True
        self.guiQueue=queue
        self.ecu = ecu()
        self.ecuData = ecuData()
        self.elmPort=openPort(self,self.portQueue)
        self.elmPort.daemon=True
 
    def run(self):
        while not self.deviceQueue.empty():
            self.deviceQueue.get_nowait()
        p = multiprocessing.current_process()
        print p.name, 'Starting', p.pid
        while not self.exit.is_set():
            print "elmDevice loop"
            try:
                contents=self.deviceQueue.get()
                self.cmd=contents[0]
                self.data=contents[1]
                print "cmd contents",self.cmd
                print "data contents",self.data
                if self.cmd == 'setSpeed':
                    self.ecu.setSpeed(self.data)
                elif self.cmd == 'setRPM':
                    self.ecu.setRPM(self.data)
                elif self.cmd == 'setRandom':
                    self.ecu.setRandom(self.data)
                elif self.cmd == 'pidCmd':
                    print 'pidCmd received',self.data
                    response = self.ecu.getEcuResponse(self.data)
                    print "ecu response is",response
                    self.portQueue.put(response)
                elif self.cmd == 'atCmd':
                    print 'atCmd received',self.data
                    response = self.atCmd(self.data)
                    print "ecu response is",response
                    self.portQueue.put(response)
                elif self.cmd == 'port':
                    guiData=[self.cmd,self.data]
                    self.guiQueue.put(guiData)
            except Queue.Empty:
                time.sleep(1)

        print p.name, 'Exiting', p.pid

    def stop(self):
        print "stopping elmDevice"
        if self.listening.is_set():
            self.elmPort.stop()
        self.exit.set()

    def putData(self,data):
        self.deviceQueue.put(data)

    def listen(self):
        self.elmPort.start()
        self.listening.set()

    def atCmd(self,data):
        print "at command"
        response = '?'
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

        return response

