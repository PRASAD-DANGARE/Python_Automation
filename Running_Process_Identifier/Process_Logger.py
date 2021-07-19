'''
Function Name    :  Process_Logger
Description      :  In This Application I Generate One Log File Of Current Running Processes And Send It Through Mail.   
Function Date    :  19 July 2021
Function Author  :  Prasad Dangare
Input            :  Get The Directory Name
Output           :  It Create One Folder Which Contains Log Files Of Current Running Processes

'''

# ===================
#
# Imports
#
# ===================

import os
import psutil
from sys import *
import Connection
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ==============================
#
# Running Process Creation Operation
#
# ==============================

def Process_Logger(FolderName = "Process-Logger"):
    
    Data = []
    
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    
    File_Path = os.path.join(FolderName,"Running-Processes.log")
    fd = open(File_Path,"w") 
    
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)

    for element in Data:
        fd.write("%s\n" % element)

    # ==============================
    #
    # Mail Sending Operation
    #
    # ==============================

    Sender_Email = 'Enter Sender Email Address'
    Receiver_Email = 'Enter Receiver Email Address'
    Password = 'Enter Sender Gmail Password'

    mail_content =  '''
                    Hello, This Mail Contains One Log File,
                    Which Contains Current Running Process On Lenovo-G50-80.
                    Thankyou....
                    '''
    
    Message = MIMEMultipart()

    Message['From'] = Sender_Email
    Message['To'] = Receiver_Email
    Message['Subject'] = 'Running Process Identifier'

    Message.attach(MIMEText(mail_content, 'plain'))

    Attach_File_Name = 'Process-Logger\\Running-Processes.log'
    Attached_File = open(Attach_File_Name, 'r') 
    
    bobj = MIMEBase('application', 'octate-stream')
    bobj.set_payload((Attached_File).read())
    encoders.encode_base64(bobj) 
    bobj.add_header('Content-Disposition', "attachment; filename = %s" % Attach_File_Name)
    Message.attach(bobj)

    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.login(Sender_Email, Password)
    text = Message.as_string()
    smtpobj.sendmail(Sender_Email, Receiver_Email, text)
    smtpobj.quit()
    
    print("Mail Successfully Sent To : ", Receiver_Email)

# =======================
#
# Entry Point
#
# =======================

def main():

    print("\n")

    print("\n\t----- Python Automation -----\n\t")
    print("\n\t---- Running Process Identifier ----\n\t")

    print("\n")
    
    print("Script Title : " + argv[0], "\n")

    if(len(argv)!=2):
        print("Insufficient Arguments\n")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name Directory_Name\n")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : It is used to create log file of running processes\n")
        exit()

    if (argv[1] != "Process-Logger"):
        exit("ERROR : Please Give Directory Name As [Process-Logger]\n")

    if((Connection.Check_Connection() == True)):
        Process_Logger(argv[1]) 

# =======================
#
# Code Starter
#
# =======================

if __name__ == "__main__":
    main()
