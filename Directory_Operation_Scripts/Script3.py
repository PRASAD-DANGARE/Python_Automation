# Design automation script which accept two directory names. Copy all files from first directory 
# into second directory. Second directory should be created at run time. 
# Usage : script3.py "Demo" "Temp"
# Demo is name of directory which is existing and contains files in it. We have to create new 
# Directory as Temp and copy all files from Demo to Temp. 

'''

Function Name    :  CPY_Dir
Description      :  Mention Above
Function Date    :  20 July 2021
Function Author  :  Prasad Dangare
Input            :  Get Old Directory Name, New Directory Name 
Output           :  Copy All Files From Old Directory Into New Directory

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

def CPY_Dir(src, dest):
    
    os.mkdir(str(dest))
    File_names = os.listdir(src)

    for File in File_names:
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

    if(len(argv) != 3):
        print("\nInsufficient Arguments to the script")
        exit()

    Source_Dir = argv[1]
    Dest_Dir = argv[2]

    CPY_Dir(Source_Dir, Dest_Dir)

# =======================
#
# Code Starter
#
# =======================

if __name__ == "__main__":
    main()
