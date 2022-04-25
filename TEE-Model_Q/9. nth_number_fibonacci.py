# find function
def find(k, n):
   f1 = 0
   f2 = 1
   i =2
   #fibonacci recursion
   while i!=0:
      f3 = f1 + f2
      f1 = f2
      f2 = f3
      if f2%k == 0:
         return n*i
      i+=1
   return
# multiple of which number
n = int(input("Enter multiple of which number: "))
# number
k = int(input("Enter the number: "))

print("Position of ",n,"\'th multiple of",k,"in Fibonacci Series is: ", find(k,n))