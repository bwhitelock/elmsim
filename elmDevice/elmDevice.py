#from multiprocessing import Process, Queue
import multiprocessing, Queue
from threading import Thread
from elmport import openPort
#import pty
import os
import time

class elmDevice (multiprocessing.Process):
    def __init__(self,queue):
        multiprocessing.Process.__init__(self)
        print "in elmDevice"
        self.deviceQueue = multiprocessing.Queue(10)
        self.exit = multiprocessing.Event()
        self.listening = multiprocessing.Event()
        #self.recvMsg = multiprocessing.Event()
        self.daemon=True
        self.returnQueue=queue
        self.elmPort=openPort(self,self.deviceQueue)
        self.elmPort.daemon=True
 
    def run(self):
        while not self.deviceQueue.empty():
            self.deviceQueue.get_nowait()
        p = multiprocessing.current_process()
        print p.name, 'Starting', p.pid
        while not self.exit.is_set():
            print "elmDevice loop"
            try:
                #contents=self.deviceQueue.get(False)
                contents=self.deviceQueue.get()
                self.item=contents[0]
                self.data=contents[1]
                print "item contents",self.item
                print "data contents",self.data
                if self.item == 'speed':
                    #self.writeCommand('test speed')
                    self.returnQueue.put('test speed')
                if self.item == 'rpm':
                    #self.writeCommand('test rpm')
                    self.returnQueue.put('test rpm')
                if self.item == 'readPort':
                    print 'readPort received',self.data
                if self.item == 'port':
                    cmd=[self.item,self.data]
                    self.returnQueue.put(cmd)
            except Queue.Empty:
                time.sleep(1)

        print p.name, 'Exiting', p.pid

    def stop(self):
        print "stopping elmDevice"
        if self.listening.is_set():
            self.elmPort.stop()
        self.exit.set()
        #self.deviceQueue.put('exit')

    def writeCommand(self,data):
        self.returnQueue.put(data)

    def putData(self,data):
        self.deviceQueue.put(data)

    def listen(self):
        self.elmPort.start()
        self.listening.set()

