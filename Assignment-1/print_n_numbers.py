num = int(input("Enter any num \'n': "))

print("The List of Natural Numbers from 1 to {0} are".format(num)) 

for i in range(1, num + 1):
    print (i, end = '  ')