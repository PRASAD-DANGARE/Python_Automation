'''
Function Name    :  mail
Description      :  This Module Connect Me To My GMAIL Account To Send The Attachment.
Function Date    :  19 July 2021
Function Author  :  Prasad Dangare
Input            :  ----
Output           :  ----

'''

# ===================
#
# Imports
#
# ===================

from Process_Logger import main
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ==============================
#
# Mail Sending Operations
#
# ==============================

def Mailing():

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
# Code Starter
#
# =======================

if __name__ == "__main__":
    main()
