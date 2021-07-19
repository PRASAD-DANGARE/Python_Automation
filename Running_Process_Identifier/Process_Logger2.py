'''
Function Name    :  ProcessDisplay
Description      :  In This Application It Generate Log Files After Every 5 Minutes And Store All Log File In Running_Process Folder   
Function Date    :  19 July 2021
Function Author  :  Prasad Dangare
Input            :  Get The Directory Name
Output           :  It Create One Folder Which Contains All Log Files Of Current Running Processes

'''

# ===================
#
# Imports
#
# ===================

import os
import time
import psutil
from sys import *
import schedule

# ==============================
#
# Running Process Creation Operation
#
# ==============================

def ProcessDisplay(FolderName = "Running_Process"):
    
    Data = []
    
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        
    File_Path = os.path.join(FolderName,"Running_Process%s.log" % time.ctime()) # due to ctime it display day,time,year and data is in string format
    File_Path = (File_Path.replace(" ","").replace(":","")) # if space is found in the path then handle it

    fd = open(File_Path,"w")
    
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)
        
    for element in Data:
        fd.write("%s\n" % element)

# =======================
#
# Entry Point
#
# =======================

def main():
    
    print("\n")
    print("------ Python Automation ------")
    print("---- Running Process Identifier ----")
    print("\n")
    
    print("Script title : "+argv[0])
    print("Folder And Log File Create After One Minute And To Close This Application Press ctrl with c")

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name Scheule_Time Directory_Name")
        exit()
      
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : It is used to create log file of running processess")
        exit()

    schedule.every(int(argv[5])).minutes.do(ProcessDisplay) # here we schdedule time as 5 minute for the log file

    while True: # create log file until the program execution is terminated
        schedule.run_pending()
        time.sleep(1)

# =======================
#
# Code Starter
#
# =======================
        
if __name__ == "__main__":
    main()
