# Python program to validate
# Indian driving license number
# using regular expression

import re

# Function to validate Indian
# driving license number.
def isValidLicenseNo(str):

	# Regex to check valid
	# Indian driving license number
	regex = ("^(([A-Z]{2}[0-9]{2})" + "( )|([A-Z]{2}-[0-9]" + "{2}))((19|20)[0-9]" + "[0-9])[0-9]{7}$")
	
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
print(isValidLicenseNo(str1))

