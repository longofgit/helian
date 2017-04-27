#!/usr/bin/python
# -*-coding:utf-8 -*-
import smtplib
import MySQLdb
import datetime
import types
def sendEmail(sender,passwd,host,port,receivers,date,mail) :
    message = MIMEText(mail, 'html', 'utf-8')
    message['From'] = Header("告警发送者<"+sender+">", 'utf-8')
    subject = str(date) + '服务器告警通知'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(host,port)
        smtpObj.ehlo()
        smtpObj.login(sender,passwd)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"
if __name__ == '__main__' :
    sender = 'liucl@helianhealth.com'
    passwd = '@Chuck20110923'
    host = 'smtp.exmail.qq.com'
    port = 465
    receivers = ['547000225@qq.com','longof@126.com']
    daytime = (datetime.date.today() - datetime.timedelta(days=1) ). strftime('%Y%m%d')
    mail = '服务器问题警报！！！'
    sendEmail(sender,passwd,host,port,receivers,daytime,mail)