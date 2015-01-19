#!/usr/bin/env python

from modeConsts import modeConsts
from mainPIDs import mainPIDs

consts = modeConsts()

data = '010C04FF'

print consts.minValue

pid = data[9:]
print "pid",pid
print mainPIDs.get('00')

print mainPIDs['0C'][consts.maxValue]

mainPIDs['0C'][consts.funcCall](None,0,0,0,'test')

print mainPIDs.get('ZQ')
