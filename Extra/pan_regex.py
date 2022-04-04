import re
 
# Function to validate the
# PAN Card number.

def isValidPanCardNo(panCardNo):
 
    # Regex to check valid
    # PAN Card number
    regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
 
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the PAN Card number
    # is empty return false
    if(panCardNo == None):
        return False
 
    # Return if the PAN Card number
    # matched the ReGex
    if(re.search(p, panCardNo) and
       len(panCardNo) == 10):
        return True
    else:
        return False
 
# Driver Code.
 
 
# Test Case 1:
str1 = input(" ")
print(isValidPanCardNo(str1))
 
