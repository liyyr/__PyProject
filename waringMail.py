#! coding:utf-8

import re
from datetime import datetime


def sendMail():
    pass


def getErrorService():
    targetFile = getTargetFile()
    f = open(targetFile, mode="r", encoding='UTF-16LE')
    lines = f.readlines()
    return re.findall('\|(.*)\|',lines[-4])[0]


def getErrorMessage():
    pass

def getDate():
    now = datetime.now()
    r = str(now)
    return r.split()[0]

def getTargetFile():
    strDatePath1 = getDate()
    strDatePath2 = str(strDatePath1.split('-')[1]) + str(strDatePath1.split('-')[2])
    targetFile = ("D:\\EastWW\\server\\log\\%s\\SMidgard_u_x64_%s_0_W.log" % (strDatePath1, strDatePath2))
    return targetFile



if __name__ == '__main__':
    getErrorService()
    #rint(getTargetFile())
    
    