#from multiprocessing import Process, Queue
import multiprocessing, Queue
import time

#itemQueue=Queue.Queue()
#dataQueue=Queue.Queue()

class elmDevice (multiprocessing.Process):
    #def __init__(self,queue):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.deviceQueue = multiprocessing.Queue(10)
        self.exit = multiprocessing.Event()
        self.recvMsg = multiprocessing.Event()
        self.daemon=True
        #self.start()
        #global itemQueue
        #itemQueue.put("init")
        #global dataQueue
        #dataQueue.put("init data")
        #self.deviceQueue.put("init")
 
    def run(self):
        #global itemQueue
        #itemQueue.put("run")
        #self.deviceQueue.acquire()
        #self.deviceQueue.Queue.clear()
        #self.deviceQueue.all_tasks_done.notify_all()
        #self.deviceQueue.unfinished_tasks = 0
        #self.deviceQueue.release()
        print "device Queue status:",self.deviceQueue.empty()
        while not self.deviceQueue.empty():
            print "removing queue item"
            self.deviceQueue.get_nowait()
        p = multiprocessing.current_process()
        print p.name, 'Starting', p.pid
        while not self.exit.is_set():
            if self.recvMsg.is_set():
                try:
                    contents=self.deviceQueue.get(False)
                    self.item=contents[0]
                    print "item in device queue is:", self.item
                    self.data=contents[1]
                    print "data in device queue is:", self.data
                except Queue.Empty:
                    print "device queue empty"
                #if not (self.item == ''):
                    #try:
                        #data=self.deviceQueue.get(False)
                        #self.data=data
                        #print "data in device queue is:", data
                    #except Queue.Empty:
                        #print "device queue empty"
                #print "test queue status:", itemQueue.empty()
                #print "data queue status:", dataQueue.empty()
                self.recvMsg.clear()
                #time.sleep(1)
            #try:
                #item=self.deviceQueue.get(False)
                #print "item in device queue is:", item
            #except Queue.Empty:
                #print "device queue empty"

            #try:
                #item=itemQueue.get(False)
                #print "item in itemQueue is:", item
            #except Queue.Empty:
                #print "item queue empty"

            #try:
                #data=dataQueue.get(False)
                #print "data in dataQueue is:", data
            #except Queue.Empty:
                #print "data queue empty"

            time.sleep(1)
        print p.name, 'Exiting', p.pid

    def stop(self):
        print "stopping process"
        self.exit.set()

    def putData(self,data):
        #self.deviceQueue.put("queueSignal")
        print "data:",data
        print "data[0]",data[0]
        print "data[1]",data[1]
        #global itemQueue
        #itemQueue.put("entry")
        #global dataQueue
        #self.deviceQueue.put("entry data")
        #self.deviceQueue.put('test')
        #self.deviceQueue.put(data[0])
        #self.deviceQueue.put(data[1])
        self.deviceQueue.put(data)
        self.recvMsg.set() 

