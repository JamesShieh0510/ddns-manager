#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
import smtplib
import init
#Create a JSON file called ./config.json and add the following json keys and values
#Tips: you can create a google app password from the URL :https://myaccount.google.com/apppasswords
# {
    # "email": "<your gmail>@gmail.com",
    # "app_token": "nmvwvbnbawgpzlgm" 
# }
#
def getSMTPProxy(email, password):
    smtp=smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, password)
    return smtp
    
def sendEmail(from_addr, to_addr, subject, content):
    config = init.config
    email = config['email']
    password = config['app_token']
    smtp=getSMTPProxy(email, password)
    msg="Subject:" + subject + "\n" + content
    status=smtp.sendmail(from_addr, to_addr, msg)#加密文件，避免私密信息被截取
    if status=={}:
        print("sended successfully!")
    else:
        print("sended failure!")
    smtp.quit()

