# Python3 program to validate passport
# number of India using regular expression
import re

# Function to validate the pin code
# of India.


def isValidPassportNo(string):

	# Regex to check valid pin code
	# of India.
	regex = "^[A-PR-WYa-pr-wy][1-9]\\d" +\
			"\\s?\\d{4}[1-9]$"

	# Compile the ReGex
	p = re.compile(regex)

	# If the string is empty
	# return false
	if (string == ''):
		return False

	# Pattern class contains matcher()
	# method to find matching between
	# given string and regular expression.
	m = re.match(p, string)

	# Return True if the string
	# matched the ReGex else False
	if m is None:
		return False
	else:
		return True


# Driver code.

# Test Case 1
str1 = input(" ")
print(isValidPassportNo(str1))

	

