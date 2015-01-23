from modeConsts import modeConsts
from mainPIDs import mainPIDs
from ecuData import ecuData

class ecu(object):
    def __init__ (self):
        self.ecuData = ecuData

    def setSpeed(self,value):
        self.ecuData.speed = value

    def getSpeed(self):
        return self.ecuData.rpm

    def setRPM(self,value):
        self.ecuData.rpm = value

    def setTemp(self,value):
        self.ecuData.temp = value

    def setRandom(self,value):
        self.ecuData.random=value

    def getSpeed(self):
        return self.ecuData.speed

    def getRPM(self):
        return self.ecuData.rpm

    def getTemp(self):
        return self.ecuData.temp

    def getRandom(self):
        return self.ecuData.random

    def getEcuResponse(self,elmCommand):
        elmCommand = elmCommand.upper()
        elmCommand = elmCommand.replace(' ','')
        response = '?'
        if len(elmCommand) == 2:
            print "mode 3 or mode 4 request"
            return "OK"
        if elmCommand[:2] == '01': #Mode 01
            pid = elmCommand[2:4]
            if not (mainPIDs.get(pid) == None):
                consts = modeConsts()
                pidMode = 1
                minVal = mainPIDs[pid][consts.minValue]
                maxVal = mainPIDs[pid][consts.maxValue]
                response=mainPIDs[pid][consts.funcCall](self,pidMode,minVal,maxVal,elmCommand)
        elif elmCommand[:2] == '02': #Mode 02
            pid = elmCommand[2:4]
            if not (mainPIDs.get(pid) == None):
                consts = modeConsts()
                pidMode = 2
                minVal = mainPIDs[pid][consts.minValue]
                maxVal = mainPIDs[pid][consts.maxValue]
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
