'''
Function Name    :  DirectoryTraversal
Description      :  This Module Travel The Directories With One Parameter Directory Name
Function Date    :  25 June 2021
Function Author  :  Prasad Dangare
Input            :  Directory Name
Output           :  Display All Files / Sub Folders Of Current Directory

'''

# ===================
# Imports
# ===================

import os
from sys import *
import CheckSum
from datetime import *

# ==============================
# Directory Traversal Operation
# ==============================

def DirectoryTraversal(path):

    print("Contents Of The Directory Are : ")

    dictionary = {}

    for Folder, SubFolder, Filename in os.walk(path):
        print("Directory Name is : " + Folder)

        for sub in SubFolder:
            print("Subfolder of " + Folder +" is "+ sub)
        
        for file in Filename:
            print("File Name is : " + file)
            
            actualpath = os.path.join(Folder, file)
            hash = CheckSum.calculateCheckSum(actualpath)

            if hash in dictionary:
                dictionary[hash].append(actualpath)
            else:
                dictionary[hash] = [actualpath]

    return dictionary

# =======================
# Entry Point
# =======================
    
def main():

    print("_____Duplicate File Removing Script_____")
    
    if(len(argv) != 2):

        print("Error : Invalid Number Of Arguments")
        exit()
    
    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("It Is A Directory Cleaner Script")
        exit()
    
    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Provide Absolute Path Of The Target Directory")
        exit()
    
    DirectoryTraversal(argv[1])

# ===================
# Starter
# ===================

if __name__=="__main__":
    main()