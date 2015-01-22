#from multiprocessing import Process, Queue
from modeConsts import modeConsts
from mainPIDs import mainPIDs
from engineControlUnits.ecuData import ecuData

class ecu(object):
    #def __init__ (self,parent):
    def __init__ (self):
        #self.parent=parent
        #print "ecu init parent",self
        #self.speed = 0
        #self.rpm = 0
        #self.temp = 0
        #self.random = False
        self.ecuData = ecuData

    def setSpeed(self,value):
        #print "set speed",speed
        #print "ecuData.speed",ecuData.speed
        self.ecuData.speed = value
        #ecuData.speed = speed
        #self.ecuData.speed = speed
        #print "speed now",self.speed
        #print "ecuData.speed",ecuData.speed

    def getSpeed(self):
        return self.ecuData.rpm

    def setRPM(self,value):
        #print "set rpm",rpm
        self.ecuData.rpm = value
        #print "rpm now",self.rpm
        #print "self",self

    def getRPM(self):
        return self.ecuData.rpm

    def setRandom(self,value):
        self.ecuData.random=value

    def getEcuResponse(self,elmCommand):
        #print "elmCommand",elmCommand
        elmCommand = elmCommand.upper()
        elmCommand = elmCommand.replace(' ','')
        response = '?'
        #print "getResponseData rpm",self.getRPM()
        #print "getResponseData speed",self.speed
        #global speedTest
        #print "global speedTest",speedTest
        if len(elmCommand) == 2:
            print "mode 3 or mode 4 request"
            return "OK"
        if elmCommand[:2] == '01': #Mode 01
            pid = elmCommand[2:4]
            #print "pid",pid
            if not (mainPIDs.get(pid) == None):
                consts = modeConsts()
                #print "consts",consts
                pidMode = 1
                #print "pidMode",pidMode
                minVal = mainPIDs[pid][consts.minValue]
                #print "minVal",minVal
                maxVal = mainPIDs[pid][consts.maxValue]
                #print "maxVal",maxVal
                #print "self",self
                #print "self.rpm",self.rpm
                response=mainPIDs[pid][consts.funcCall](self,pidMode,minVal,maxVal,elmCommand)
        elif elmCommand[:2] == '02': #Mode 02
            pid = elmCommand[2:4]
            #print "pid",pid
            if not (mainPIDs.get(pid) == None):
                consts = modeConsts()
                #print "consts",consts
                pidMode = 2
                #print "pidMode",pidMode
                minVal = mainPIDs[pid][consts.minValue]
                #print "minVal",minVal
                maxVal = mainPIDs[pid][consts.maxValue]
                #print "maxVal",maxVal
                response=mainPIDs[pid][consts.funcCall](self,pidMode,minVal,maxVal,elmCommand)
        elif elmCommand[:2] == '05': #Mode 05
            response='OK'
        elif elmCommand[:2] == '06': #Mode 06
            response='OK'
        elif elmCommand[:2] == '07': #Mode 07
            response='OK'
        elif elmCommand[:2] == '08': #Mode 08
            response='OK'
        elif elmCommand[:2] == '09': #Mode 09
            response='OK'
        elif elmCommand[:2] == '0A': #Mode 0A
            response='OK'

        return response
