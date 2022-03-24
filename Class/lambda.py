List = [[3,4,1],[8,4,10,3]]

sortList = lambda x: (sorted(i) for i in x)

secondLargest = lambda x,f:[y[len(y)-7] for y in f(x)]

res=secondLargest(List, sortList)
print(res)

