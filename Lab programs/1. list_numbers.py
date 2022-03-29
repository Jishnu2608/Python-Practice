l = []
rng1=int(input("Enter the lower range: "))
rng2=int(input("Enter the upper range: "))

for i in range(rng1,rng2):
    l.append(i)

print("List with integers from",rng1,"to",rng2,"is: ")
print(l)