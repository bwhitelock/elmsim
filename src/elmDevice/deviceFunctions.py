from atCommands import atCommands
from deviceFunctions import *

def setSpeed(parent,data):
    print "Speed"
    parent.ecu.setSpeed(data)

def setRPM(parent,data):
    print "setRPM"
    parent.ecu.setRPM(data)

def setTemp(parent,data):
    print "setTemp"
    parent.ecu.setTemp(data)

def setRandom(parent,data):
    print "setRandom"
    parent.ecu.setRandom(data)
    print "random is",parent.ecu.getRandom()

def elmPort(parent,data):
    print "elmPort"
    guiData=['elmPort',data]
    parent.guiQueue.put(guiData)

def pidCmd(parent,data):
    print "pidCmd"
    #parent.ecu.setRandom(data)
    response = parent.ecu.getEcuResponse(data)
    parent.portQueue.put(response)

def atCmd(parent,data):
    print "atCmd"
    response = '?'
    if atCommands.get(data[:6]):
        print "using dict call",atCommands[data[:6]]
        response=atCommands[data[:6]](parent)
        print "dict response",response
    elif atCommands.get(data[:5]):
        print "using dict call",atCommands[data[:5]]
        response=atCommands[data[:5]](parent)
        print "dict response",response
    elif atCommands.get(data[:4]):
        print "using dict call",atCommands[data[:4]]
        response=atCommands[data[:4]](parent)
        print "dict response",response
    elif atCommands.get(data[:3]):
        print "using dict call",atCommands[data[:3]]
        response=atCommands[data[:3]](parent)
        print "dict response",response
    elif atCommands.get(data):
        print "using dict call",atCommands[data]
        response=atCommands[data](parent)
        print "dict response",response

    parent.portQueue.put(response)
