'''
Function Name    :  DirectoryTraversal, DisplayDuplicate
Description      :  In This Application We Import All Other Modules To Perform Duplicate Files Removing Operation
Function Date    :  25 June 2021
Function Author  :  Prasad Dangare
Input            :  Get The Directory Name
Output           :  Delete Duplicate Files And Create Log File And Send It Through Mail To The User / Client.

'''

# ===================
# Imports
# ===================

import os
from sys import *
import CheckSum, log_File, Mailing, Connection
from datetime import *

# ==============================
# Directory Traversal Operations
# ==============================

def DirectoryTraversal(path):

    print("\nContents of the Directory are : ")

    dictionary = {}

    for Folder, SubFolder, Filename in os.walk(path):
        print("\nDirectory Name is : " + Folder)

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

    current_date_time = datetime.now().strftime("%d_%m_%Y-%I_%M")+".txt"

    log_File.Writing(dictionary, current_date_time)
    Show = DisplayDuplicate(dictionary)
    
    Mailing.mail(current_date_time)

    return dictionary

# ==================================
# Display Directory Files Operations 
# ==================================


def DisplayDuplicate(dictionary):

    output = list(filter(lambda x : len(x) > 1, dictionary.values()))

    if(len(output) > 0):
        print("\nThere Are Duplicate Files")
    else:
        print("\nThere Are No Dupicate Files")
        return
    
    print("\nList Of Duplicate Files Are : \n")

    i = 0
    icnt = 0

    for result in output:

        icnt = 0
        print(result)
        for path in result:
            icnt += 1 # skip 1 file
            if  icnt >= 2:
                i += 1
                #print("%s"%path)
                os.remove(path)
                # here type logic for delete the duplicate files

    print("\nNumber Of Duplicate Files Deleted ", i)

# =======================
# Entry Point
# =======================

def main():

    print("\n\t_____Duplicate File Removing Script_____\n\t")
    
    if(len(argv) != 2):

        print("Error : Invalid Number Of Arguments")
        exit()
    
    if((argv[1] == "-h") or (argv[1] == "-H")):
        
        print("It Is A Directory Cleaner Script")
        exit()
    
    if((argv[1] == "-u") or (argv[1] == "-U")):

        print("Usage : Provide Absolute Path Of The Target Directory")
        exit()
    
    path = os.path.join(os.getcwd(), argv[1])

    if((os.path.isdir(path) == True) and (Connection.Check_Connection() == True)):
        DirectoryTraversal(argv[1])

# ===================
# Starter
# ===================

if __name__=="__main__":
    main()