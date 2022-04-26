import re

file1 = open('input1.txt',
		'r')

file2 = open('input.txt','w')

for line in file1.readlines():

	x = re.findall("^Geeks", line)
	
	if not x:
		
		print(line)
		
		file2.write(line)

file1.close()
file2.close()
	
#https://www.geeksforgeeks.org/how-to-remove-lines-starting-with-any-prefix-using-python/