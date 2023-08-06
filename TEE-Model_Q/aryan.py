x=input("Enter the character : ")
count =0
f=open('test.txt','r')
text=f.read()
for i in text:
    if(i==x):
        count+=1
print(text, count)
