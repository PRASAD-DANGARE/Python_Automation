'''
Function Name    :  Writing, Duplicate_Writing
Description      :  This Module Create / Maintain The Log File Of Duplicate Files
Function Date    :  25 June 2021
Function Author  :  Prasad Dangare
Input            :  ----
Output           :  ----

'''

# ===================
# Imports
# ===================

import os
from sys import *

# ==============================
# Writing Operation
# ==============================

Filepath = os.getcwd()

def Writing(dictionary, current_date_time):

    file_Name = os.path.join(Filepath, current_date_time)
    fd = open(file_Name, 'w') 

    for key, value in dictionary.items(): 
        fd.write('%s:%s\n' % (key, value))
    
    fd.close()

# ======================================
# Duplicate Files Writing Operation
# ======================================

def Duplicate_Writing(lister):
    
    Filename = os.path.join(Filepath, "duplicate_Files.txt")
    fd = open(Filename, 'w') 
    
    for value in lister.items(): 
        fd.write('%s\n' % (value))
    
    fd.close()