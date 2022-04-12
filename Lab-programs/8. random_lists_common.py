import random

n=int(input("Enter length of first list: "))
n1=int(input("Enter length of second list: "))
 
one = random.sample(range(1, 100), n)
two = random.sample(range(1, 100), n1)

print ("Random number list 1 is : " +  str(one))
print ("Random number list 2 is : " +  str(two))

both=[]

if len(one) < len(two):
    for i in one:
        if i in two and i not in both:
            both.append(i)
         
if len(one) > len(two):
    for i in two:
        if i in one and i not in both:
            both.append(i)
                     
print("Common elements in both list(s) is: ",both)