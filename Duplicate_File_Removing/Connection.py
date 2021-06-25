'''
Function Name    :  Check_Connection
Description      :  This Module Check The Internet Status For Connection
Function Date    :  25 June 2021
Function Author  :  Prasad Dangare
Input            :  ----
Output           :  ----

'''

# ===================
# Imports
# ===================

from urllib.request import urlopen

try:
        urlopen('http://www.google.com', timeout = 1)
        print("\nMail Successfully Send...")
except:
        print("\nPlease Check Your Internet Connection")

# ==============================
# Check Connection
# ==============================

def Check_Connection():

    try:
        urlopen('http://www.google.com', timeout = 1)
        return True
    except:
        return False
