test_list = [32, 67, 98, 34]

print("The original list is : " + str(test_list))
 
res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), test_list))
     
total = 0

for ele in range(0, len(res)):
    total = total + res[ele]
 
# printing total value

print("Sum of all digits of elements in given list: ", total)