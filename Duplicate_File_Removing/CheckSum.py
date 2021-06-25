'''
Function Name    :  calculateCheckSum
Description      :  This Module Calculate The Check Sum Of Each File
Function Date    :  25 June 2021
Function Author  :  Prasad Dangare
Input            :  ----
Output           :  ----

'''

# ===================
# Imports
# ===================

import hashlib

# ==============================
# Calculate Checksum Operation
# ==============================

def calculateCheckSum(path, blocksize = 1024):

    fd = open(path,'rb')
    hobj = hashlib.md5()

    buffer = fd.read(blocksize)
    
    while len(buffer) > 0:

        hobj.update(buffer)
        buffer = fd.read(blocksize)
    
    fd.close()

    return hobj.hexdigest()