#!/usr/bin/env python

from random import randrange as rand
#value = random.randrange(1,15)
value = rand(1,15)
print value
print "%X" % value

#data = "%X%X%X%X%X%X%X%X" % (11,15,15,15,15,15,15,15)
data = "%X%X%X%X%X%X%X%X" % (8+rand(1,3),rand(1,15),rand(1,15),rand(1,15),rand(1,15),rand(1,15),rand(1,15),rand(1,15))

print data

minVal = 0
maxVal = 0

if (minVal == maxVal) and (minVal == 0):
    print "min and max 0"

print "%02X" % -40
