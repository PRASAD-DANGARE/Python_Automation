# Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion
# Usage : script2.py "Demo" ".txt" ".py" 
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc. 
# After execution this script each .txt file gets renamed as .doc. 

'''

Function Name    :  Change_Ext
Description      :  Mention Above
Function Date    :  20 July 2021
Function Author  :  Prasad Dangare
Input            :  Get The Directory Name, Old File Extension, New File Extension
Output           :  Change All Files Extension Into New File Extension

'''

# ===================
#
# Imports
#
# ===================

import os
from sys import *

# ==============================
#
# Change Extensions Operation
#
# ==============================

def Change_Ext(path, Old_Ext, New_Ext):

    for Filename in os.listdir(path):

        Infilename = os.path.join(path, Filename)

        if not os.path.isfile(Infilename): 
            continue
        
        OldFileExt = os.path.splitext(Filename)
        NewFileExt = Infilename.replace(Old_Ext, New_Ext)
        Result = os.rename(Infilename, NewFileExt)

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

    Change_Ext(argv[1], argv[2], argv[3])

# =======================
#
# Code Starter
#
# =======================

if __name__ == "__main__":
    main()
