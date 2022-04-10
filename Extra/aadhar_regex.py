import re
 
# Function to validate Aadhaar
# number.
def isValidAadhaarNumber(str):
 
    # Regex to check valid
    # Aadhaar number.
    regex = ("^[2-9]{1}[0-9]{3}\\" +"s[0-9]{4}\\s[0-9]{4}$")
     
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty
    # return false
    if (str == None):
        return False
 
    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False
 
# Driver code
 
# Test Case 1:
str1 = input(" ")
print(isValidAadhaarNumber(str1))
 
