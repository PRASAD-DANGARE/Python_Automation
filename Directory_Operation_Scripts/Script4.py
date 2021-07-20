# Design automation script which accept two directory names and one file extension. Copy all 
# files with the specified extension from first directory into second directory. Second directory 
# should be created at run time.
# Usage : script4.py "Demo" "Temp" ".exe"
# Demo is name of directory which is existing and contains files in it. We have to create new 
# Directory as Temp and copy all files with extension .exe from Demo to Temp.

'''

Function Name    :  CPY_Dir
Description      :  Mention Above
Function Date    :  20 July 2021
Function Author  :  Prasad Dangare
Input            :  Get Old Directory Name, New Directory Name, File Extension
Output           :  Copy Only Those Files From Old Directory Into New Directory Whose File Extension Matches 

'''

# ===================
#
# Imports
#
# ===================

import shutil
import os
from sys import *

# ==============================
#
# Copy Folder Operation
#
# ==============================

def CPY_Dir(src, dest, Ext):
    
    os.mkdir(str(dest))
    File_names = os.listdir(src)

    for File in File_names:
        if Ext in File:
            shutil.copy(os.path.join(src, File), dest)

    print("Successfully Done...\n")

# =======================
#
# Entry Point
#
# =======================

def main():

    print("\n\t----- Automation Script -----\n\t")
    print("ScriptTitle : " + argv[0])

    if(len(argv) != 4):
        print("\nInsufficient Arguments to the script")
        exit()

    Source_Dir = argv[1]
    Dest_Dir = argv[2]
    File_Ext = argv[3]

    CPY_Dir(Source_Dir, Dest_Dir, File_Ext)

# =======================
#
# Code Starter
#
# =======================

if __name__ == "__main__":
    main()


