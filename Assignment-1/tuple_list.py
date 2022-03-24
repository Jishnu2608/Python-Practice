print("------------------Tuple---------------------")
t1=(1,2,100,34.8,"ram")
t2=(10,20,30,"block",45.9)
print(t1)
print(t2)
print(t1+t2)
print(t1[3]+t2[2])
print(t1[2:]) #slicing
print(t1[2:5])
print(t1[2:6])
print(t1*3) #repetition

a=34.8 in t1
print(a)
#tuple packing
(a,b,c,d)=(120,128.5,34,1000)
print(a)
print(b)
print(c)
print(d)
print("------------------List---------------------")
list1=['20BCE10001','20BCE10002','20BCE10003','20BCE10004','20BCE10005','20BCE10006','20BCE10007','20BCE10008','20BCE10009','20BCE10010']
list2=['name1','name2','name3','name4','name5','name6','name7','name8','name9','name10']
print(list1+list2)
print(list1[3])

print(list1[2]+list2[2])
print(list1[2:])
print(list2[:2])
print(list2*3)
m1=12 in list1
print(m1)
m2="Indiaa" in list1
print(m2)
m3=100 not in list2
print(m3)
#insertion
list1.insert(3,"usa")
print(list1)
list2.insert(2,12000)
print(list2)
#updation
list2[4]="waterland"
print(list2)
list1[3]=10000
print(list1)
#removing
list2.remove(list2[1])
print(list2)
m4="India" and "coolest" in list1
print(m4)


