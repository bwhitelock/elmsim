from random import randrange as rand

def randomBytes1():
    #print "randomBytes1"
    bytesData = "%02X" % rand(0,255)
    #print "bytesData",bytesData
    return bytesData

def randomBytes2():
    #print "randomBytes2"
    bytesData = "%02X%02X" % (rand(0,255),rand(0,255))
    return bytesData

def randomBytes3():
    #print "randomBytes3"
    bytesData = "%02X%02X%02X" % (rand(0,255),rand(0,255),rand(0,255))
    return bytesData

def randomBytes4():
    #print "randomBytes4"
    bytesData = "%02X%02X%02X%02X" % (rand(0,255),rand(0,255),rand(0,255),rand(0,255))
    return bytesData

def modeFunc_00(parent,pidMode,minValue,maxValue,data):
    #print "modeFunc_00"
    if pidMode == 1:
        #print "mode 1 pid 00"
        response = "%X%X%X%X%X%X%X%X" % (8+rand(1,3),rand(1,15),rand(1,15),rand(1,15),rand(1,15),rand(1,15),rand(1,15),rand(1,15))
        response = '4100' + response
        #print "response should be",response
    elif pidMode == 2:
        #print "mode 2 pid 00"
        response = "%X%X%X%X%X%X%X%X" % (4+rand(1,3),rand(1,15),rand(1,15),rand(1,15),rand(1,15),rand(1,15),rand(1,15),rand(1,15))
        response = '4200' + response
        #print "response should be",response
    else:
        response = '?'
    return response

def modeFunc_01(parent,pidMode,minValue,maxValue,data):
    #print "modeFunc_01"
    if pidMode == 1:
        response = "0077FFFF" #simulate mill off, 0 DTCs, spark ignition and all tests available and complete
        response = '4101' + response
    else:
        response = '?'
    return response

def modeFunc_02(parent,pidMode,minValue,maxValue,data):
    #print "modeFunc_02"
    if pidMode == 2:
        response = "0000" #simulate no DTC set
        response = '4202' + response
    else:
        response = '?'
    return response

def modeFunc_03(parent,pidMode,minValue,maxValue,data):
    #print "modeFunc_03"
    response = '02' #simulate closed loop O2 normal feedback
    #response = "%s%s%s" % ((40+pidMode),'03', response)
    response = "%s%s%s" % ((40+pidMode),data[2:4], response)
    return response

def modeFunc_04(parent,pidMode,minValue,maxValue,data):
    #print "modeFunc_04"
    #response = "%02X" % rand(0,255)
    response = randomBytes1()
    response = "%s%s%s" % ((40+pidMode),data[2:4], response)
    return response

def modeFunc_05(parent,pidMode,minValue,maxValue,data):
    #print "modeFunc_05"
    #response = "%02X" % rand(0,255)
    response = randomBytes1()
    response = "%s%s%s" % ((40+pidMode),data[2:4], response)
    return response

def modeFunc_06(parent,pidMode,minValue,maxValue,data):
    #print "modeFunc_06"
    #response = "%02X" % rand(0,255)
    response = randomBytes1()
    response = "%s%s%s" % ((40+pidMode),data[2:4], response)
    return response

def modeFunc_07(parent,pidMode,minValue,maxValue,data):
    #print "modeFunc_07"
    response = randomBytes1()
    response = "%s%s%s" % ((40+pidMode),data[2:4], response)
    return response

def modeFunc_08(parent,pidMode,minValue,maxValue,data):
    #print "modeFunc_08"
    response = randomBytes1()
    response = "%s%s%s" % ((40+pidMode),data[2:4], response)
    return response

def modeFunc_09(parent,pidMode,minValue,maxValue,data):
    #print "modeFunc_09"
    response = randomBytes1()
    response = "%s%s%s" % ((40+pidMode),data[2:4], response)
    return response

def modeFunc_0A(parent,pidMode,minValue,maxValue,data):
    #print "modeFunc_0A"
    response = randomBytes1()
    response = "%s%s%s" % ((40+pidMode),data[2:4], response)
    return response

def modeFunc_0B(parent,pidMode,minValue,maxValue,data):
    #print "modeFunc_0B"
    response = randomBytes1()
    response = "%s%s%s" % ((40+pidMode),data[2:4], response)
    return response

def modeFunc_0C(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_0C"
    if parent.ecuData.random:
        response = randomBytes2()
    else:
        response = "%04X" % int(parent.ecuData.rpm)
    print response
    response = "%s%s%s" % ((40+pidMode),data[2:4], response)
    return response

def modeFunc_0D(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_0D"
    if parent.ecuData.random:
        response = randomBytes1()
    else:
        response = "%02X" % int(parent.ecuData.speed)
    print response
    response = "%s%s%s" % ((40+pidMode),data[2:4], response)
    return response

def modeFunc_0E(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_0E"
    return "OK"

def modeFunc_0F(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_0F"
    return "OK"

def modeFunc_10(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_10"
    return "OK"

def modeFunc_11(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_11"
    return "OK"

def modeFunc_12(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_12"
    return "OK"

def modeFunc_13(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_13"
    return "OK"

def modeFunc_14(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_14"
    return "OK"

def modeFunc_15(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_15"
    return "OK"

def modeFunc_16(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_16"
    return "OK"

def modeFunc_17(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_17"
    return "OK"

def modeFunc_18(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_18"
    return "OK"

def modeFunc_19(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_19"
    return "OK"

def modeFunc_1A(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_1A"
    return "OK"

def modeFunc_1B(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_1B"
    return "OK"

def modeFunc_1C(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_1C"
    return "OK"

def modeFunc_1D(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_1D"
    return "OK"

def modeFunc_1E(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_1E"
    return "OK"

def modeFunc_1F(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_1F"
    return "OK"

def modeFunc_20(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_20"
    return "OK"

def modeFunc_21(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_21"
    return "OK"

def modeFunc_22(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_22"
    return "OK"

def modeFunc_23(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_23"
    return "OK"

def modeFunc_24(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_24"
    return "OK"

def modeFunc_25(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_25"
    return "OK"

def modeFunc_26(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_26"
    return "OK"

def modeFunc_27(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_27"
    return "OK"

def modeFunc_28(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_28"
    return "OK"

def modeFunc_29(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_29"
    return "OK"

def modeFunc_2A(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_2A"
    return "OK"

def modeFunc_2B(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_2B"
    return "OK"

def modeFunc_2C(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_2C"
    return "OK"

def modeFunc_2D(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_2D"
    return "OK"

def modeFunc_2E(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_2E"
    return "OK"

def modeFunc_2F(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_2F"
    return "OK"

def modeFunc_30(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_30"
    return "OK"

def modeFunc_31(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_31"
    return "OK"

def modeFunc_32(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_32"
    return "OK"

def modeFunc_33(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_33"
    return "OK"

def modeFunc_34(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_34"
    return "OK"

def modeFunc_35(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_35"
    return "OK"

def modeFunc_36(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_36"
    return "OK"

def modeFunc_37(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_37"
    return "OK"

def modeFunc_38(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_38"
    return "OK"

def modeFunc_39(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_39"
    return "OK"

def modeFunc_3A(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_3A"
    return "OK"

def modeFunc_3B(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_3B"
    return "OK"

def modeFunc_3C(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_3C"
    return "OK"

def modeFunc_3D(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_3D"
    return "OK"

def modeFunc_3E(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_3E"
    return "OK"

def modeFunc_3F(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_3F"
    return "OK"

def modeFunc_40(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_40"
    return "OK"

def modeFunc_41(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_41"
    return "OK"

def modeFunc_42(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_42"
    return "OK"

def modeFunc_43(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_43"
    return "OK"

def modeFunc_44(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_44"
    return "OK"

def modeFunc_45(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_45"
    return "OK"

def modeFunc_46(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_46"
    return "OK"

def modeFunc_47(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_47"
    return "OK"

def modeFunc_48(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_48"
    return "OK"

def modeFunc_49(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_49"
    return "OK"

def modeFunc_4A(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_4A"
    return "OK"

def modeFunc_4B(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_4B"
    return "OK"

def modeFunc_4C(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_4C"
    return "OK"

def modeFunc_4D(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_4D"
    return "OK"

def modeFunc_4E(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_4E"
    return "OK"

def modeFunc_4F(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_4F"
    return "OK"

def modeFunc_50(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_50"
    return "OK"

def modeFunc_51(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_51"
    return "OK"

def modeFunc_52(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_52"
    return "OK"

def modeFunc_53(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_53"
    return "OK"

def modeFunc_54(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_54"
    return "OK"

def modeFunc_55(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_55"
    return "OK"

def modeFunc_56(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_56"
    return "OK"

def modeFunc_57(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_57"
    return "OK"

def modeFunc_58(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_58"
    return "OK"

def modeFunc_59(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_59"
    return "OK"

def modeFunc_5A(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_5A"
    return "OK"

def modeFunc_5B(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_5B"
    return "OK"

def modeFunc_5C(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_5C"
    return "OK"

def modeFunc_5D(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_5D"
    return "OK"

def modeFunc_5E(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_5E"
    return "OK"

def modeFunc_5F(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_5F"
    return "OK"

def modeFunc_60(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_60"
    return "OK"

def modeFunc_61(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_61"
    return "OK"

def modeFunc_62(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_62"
    return "OK"

def modeFunc_63(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_63"
    return "OK"

def modeFunc_64(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_64"
    return "OK"

def modeFunc_65(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_65"
    return "OK"

def modeFunc_66(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_66"
    return "OK"

def modeFunc_67(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_67"
    return "OK"

def modeFunc_68(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_68"
    return "OK"

def modeFunc_69(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_69"
    return "OK"

def modeFunc_6A(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_6A"
    return "OK"

def modeFunc_6B(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_6B"
    return "OK"

def modeFunc_6C(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_6C"
    return "OK"

def modeFunc_6D(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_6D"
    return "OK"

def modeFunc_6E(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_6E"
    return "OK"

def modeFunc_6F(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_6F"
    return "OK"

def modeFunc_70(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_70"
    return "OK"

def modeFunc_71(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_71"
    return "OK"

def modeFunc_72(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_72"
    return "OK"

def modeFunc_73(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_73"
    return "OK"

def modeFunc_74(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_74"
    return "OK"

def modeFunc_75(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_75"
    return "OK"

def modeFunc_76(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_76"
    return "OK"

def modeFunc_77(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_77"
    return "OK"

def modeFunc_78(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_78"
    return "OK"

def modeFunc_79(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_79"
    return "OK"

def modeFunc_7A(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_7A"
    return "OK"

def modeFunc_7B(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_7B"
    return "OK"

def modeFunc_7C(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_7C"
    return "OK"

def modeFunc_7D(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_7D"
    return "OK"

def modeFunc_7E(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_7E"
    return "OK"

def modeFunc_7F(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_7F"
    return "OK"

def modeFunc_80(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_80"
    return "OK"

def modeFunc_81(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_81"
    return "OK"

def modeFunc_82(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_82"
    return "OK"

def modeFunc_83(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_83"
    return "OK"

def modeFunc_84(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_84"
    return "OK"

def modeFunc_85(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_85"
    return "OK"

def modeFunc_86(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_86"
    return "OK"

def modeFunc_87(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_87"
    return "OK"

def modeFunc_A0(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_A0"
    return "OK"

def modeFunc_C0(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_C0"
    return "OK"

def modeFunc_C3(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_C3"
    return "OK"

def modeFunc_C4(parent,pidMode,minValue,maxValue,data):
    print "modeFunc_C4"
    return "OK"
