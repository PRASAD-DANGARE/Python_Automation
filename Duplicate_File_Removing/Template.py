'''
Function Name    :  main()
Description      :  This Module Contain Application Template (Usage, Help) About This Application
Function Date    :  25 June 2021
Function Author  :  Prasad Dangare
Input            :  Directory Path
Output           :  ----

'''

# ===================
# Imports
# ===================

import os
from sys import *

# =======================
# Entry Point
# =======================

def main():

    print("\n\t_____Duplicate File Removing Script_____\n\t")

    if(len(argv) != 2):
        print("Error : Invalid Number Of Arguments")
        exit()

    if((argv[1] == "-h")or(argv[1] == "-H")):
        print("It Is A Directory Cleaner Script")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Provide Absolute Path Of The Target Directory")
        exit()
    
# ===================
# Starter
# ===================

if __name__=="__main__":
    main()