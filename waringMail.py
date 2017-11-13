#!/usr/bin/python
# -*- coding: UTF-8 -*-


import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime


def sendMail(serviceName):
    # 第三方 SMTP 服务
    mail_host="smtp.ym.163.com"  #设置服务器
    mail_user="xxx@eastfantasy.com"    #用户名
    mail_pass="xxxx"   #口令 
     
    sender = 'xxx@eastfantasy.com'
    receivers = ['aaa@eastfantasy.com', '123456@qq.com']      #接收邮件，可设置为你的QQ邮箱或者其他邮箱
     
    message = MIMEText('%s 服务端出现故障,请赶紧处理' % serviceName , 'plain', 'utf-8')
    message['From'] = Header("报警监控", 'utf-8')
    message['To'] =  Header("全体成员", 'utf-8')
     
    subject = '测试服 %s 服务端出现故障' % serviceName
    message['Subject'] = Header(subject, 'utf-8')
      
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        #print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

def getErrorService():
    targetFile = getTargetFile()
    f = open(targetFile, mode="r", encoding='UTF-16LE')
    lines = f.readlines()
    index = -1
    while(index != 0):      #while循环，从文本最后一行开始遍历，直至查询到的第一个符合要求内容，停止查询退出，返回结果
        try:
            ErrorServiceName = re.findall('\|(.*)\|',lines[index])[0]
            index = 0
        except:
            index -= 1
    return ErrorServiceName

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
    name = getErrorService()
    sendMail(name)
    #print(getTargetFile())
    #print(getErrorService())
    
    