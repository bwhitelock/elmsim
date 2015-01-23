import multiprocessing, Queue
from threading import Thread
from elmport import openPort
import os
import time
from ecu.ecu import ecu
from ecu.ecuData import ecuData
from atCommands import atCommands
from deviceCommands import deviceCommands

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
                if deviceCommands.get(self.cmd):
                    deviceCommands[self.cmd](self,self.data)
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
