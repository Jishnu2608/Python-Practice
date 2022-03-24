arr=[]
n=int(input("Number of elements in array:"))
for i in range(0,n):
   l=int(input())
   arr.append(l)
print("The given array is:",arr)     
sum = 0;    
     
#Loop through the array to calculate sum of elements    
for i in range(0, len(arr)):    
   sum = sum + arr[i];    
     
print("Sum of all the elements of an array: " + str(sum));    