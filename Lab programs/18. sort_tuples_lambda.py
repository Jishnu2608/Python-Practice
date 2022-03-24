def Sort_Tuple(tup): 

    tup.sort(key = lambda x: x[1]) 
    return tup 
  
tup = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
  
# printing the sorted list of tuples
print(Sort_Tuple(tup)) 