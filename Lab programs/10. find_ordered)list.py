def find(ordered_list, element_to_find):

  for element in ordered_list:
    if element == element_to_find:
      return True
  return False
  
if __name__=="__main__":
    
    lst = []
 
    n = int(input("Enter number of elements : "))

    for i in range(0, n):
        ele = int(input())
    
        lst.append(ele) 
        
    print(lst)
    
    key=int(input("Enter the number to be searched: "))
    
    print(find(lst, key)) 
  