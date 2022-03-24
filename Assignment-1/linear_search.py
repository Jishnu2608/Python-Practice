def linear_Search(list1, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
list1=[]
num=int(input("Number of elements in array:"))
for i in range(0,num):
   l=int(input())
   list1.append(l)
print("The given array is:",list1)       

key=int(input("Enter the element to be searched: ")) 
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)  