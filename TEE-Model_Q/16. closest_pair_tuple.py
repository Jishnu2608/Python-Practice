test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
  
tup = (17, 23)
  
K=1

res = min(range(len(test_list)), key = lambda sub: abs(test_list[sub][K - 1] - tup[K - 1]))

print("The nearest tuple to Kth index element is : " + str(test_list[res])) 
