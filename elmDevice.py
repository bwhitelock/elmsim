#from multiprocessing import Process, Queue
import multiprocessing, Queue
import time

class elmDevice (multiprocessing.Process):
    def __init__(self,queue):
        multiprocessing.Process.__init__(self)
        self.deviceQueue = multiprocessing.Queue(10)
        self.exit = multiprocessing.Event()
        #self.recvMsg = multiprocessing.Event()
        self.daemon=True
        self.returnQueue=queue
 
    def run(self):
        while not self.deviceQueue.empty():
            self.deviceQueue.get_nowait()
        p = multiprocessing.current_process()
        print p.name, 'Starting', p.pid
        while not self.exit.is_set():
            try:
                contents=self.deviceQueue.get(False)
                self.item=contents[0]
                self.data=contents[1]
                if self.item == 'speed':
                    #self.writeCommand('test speed')
                    self.returnQueue.put('test speed')
                if self.item == 'rpm':
                    #self.writeCommand('test rpm')
                    self.returnQueue.put('test rpm')
            except Queue.Empty:
                time.sleep(1)
        print p.name, 'Exiting', p.pid

    def stop(self):
        print "stopping process"
        self.exit.set()

    def writeCommand(self,data):
        self.returnQueue.put(data)

    def putData(self,data):
        self.deviceQueue.put(data)

