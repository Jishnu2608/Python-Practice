x=int(input("Enter any non negative number: "))
fact=1
i=1
for i in range(1,x+1):
    fact=fact*i
    i=i+1
print("Factorial of",x,"is:", fact)
