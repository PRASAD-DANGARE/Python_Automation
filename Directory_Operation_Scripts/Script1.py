# Design automation script which accept directory name and file extension from user, Display all files with that extension
# Usage : script1.py "Demo" ".txt"
# Demo is name of directory and .txt is the extension that we want to search. 

'''

Function Name    :  Display_Ext
Description      :  Mention Above
Function Date    :  20 July 2021
Function Author  :  Prasad Dangare
Input            :  Get The Directory Name, File Extension
Output           :  Display Searched Extension Files

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
# Display Extensions Operation
#
# ==============================

def Display_Ext(path, ext):

    print("\nList Of Searched Extension", ext, "Files Are : \n")

    Data = []

    for (root, dirs, file) in os.walk(path):
        for F in file:
            if ext in F:
                Data.append(F)

    return Data

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

    Dir_Name = argv[1]
    File_Ext = argv[2]

    arr = Display_Ext(Dir_Name, File_Ext)

    print("Successfully Done...\n")
    for Elements in arr:
        print(Elements)

# =======================
#
# Code Starter
#
# =======================

if __name__ == "__main__":
    main()
