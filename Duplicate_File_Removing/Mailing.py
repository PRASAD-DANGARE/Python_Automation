'''
Function Name    :  mail
Description      :  This Module Connect Me To My GMAIL Account To Send The Attachment.
Function Date    :  25 June 2021
Function Author  :  Prasad Dangare
Input            :  ----
Output           :  ----

'''

# ===================
# Imports
# ===================

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime

# ==============================
# Mail Sending Operations
# ==============================

def mail(current_date_time):

    Sender_email = "Sender Mail ID"
    Receiver_email = "Receiver Mail ID"
    Password = "...."
   
    mobj = MIMEMultipart() # object created of MIMEMultipart
    
    mobj['From'] = Sender_email
  
    mobj['To'] = Receiver_email
  
    mobj['Subject'] = "Duplicate Files Removing Notifier"
  
    body = "Attached txt File Contain Duplicate File Names And There Hashcodes Detected On : " + datetime.now().strftime("%d_%m_%Y-%I_%M") + " This All Duplicate Files Are Now Deleted As Mention In The Attachment"

    mobj.attach(MIMEText(body, 'plain')) # Attaching The Body for MIMEMultipart Object
  
    filename = "24_06_2021-05_11.txt" # File Name To Be Send 
    attachment = open(os.getcwd()+"\\"+current_date_time, 'r')
  
    bobj = MIMEBase('application', 'octet-stream') # create object of MIMEBase as bobj
  
    bobj.set_payload((attachment).read()) # change the payload into encoded form
  
    encoders.encode_base64(bobj) # encode into base64
   
    bobj.add_header('Content-Disposition', "attachment; filename = %s" % filename)
  
    mobj.attach(bobj) # attaching the object of bobj to  mobj
  
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session, outgoing smtp server for gmail (smtp.gmail.com) 
  
    smtpobj.ehlo() # identify computer

    smtpobj.starttls() # started the TLS for security (transport layer security)
  
    smtpobj.login(Sender_email, Password)

    text = mobj.as_string() # Converts the Multipart mobj into a string
  
    smtpobj.sendmail(Sender_email, Receiver_email, text)
  
    smtpobj.quit() # terminating the session