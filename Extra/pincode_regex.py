# Python3 program to validate the
# pin code of India using Regular
# Expression.
import re

# Function to validate the pin code
# of India.
def isValidPinCode(pinCode):
	
	# Regex to check valid pin code
	# of India.
	regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"

	# Compile the ReGex
	p = re.compile(regex)
	
	# If the pin code is empty
	# return false
	if (pinCode == ''):
		return False
		
	# Pattern class contains matcher() method
	# to find matching between given pin code
	# and regular expression.
	m = re.match(p, pinCode)
	
	# Return True if the pin code
	# matched the ReGex else False
	if m is None:
		return False
	else:
		return True

# Driver code

# Test case 1
num1 = "132103"
print(num1, ": ", isValidPinCode(num1))
	
	