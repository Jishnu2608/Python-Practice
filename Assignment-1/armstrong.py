num = int(input("Enter a number: "))
 
order = len(str(num))   
             
sum = 0                                         
temp = num                  
            
while temp > 0:                                     
    n = temp % 10
    temp = temp // 10
    sum = sum + pow(n,order)   
           
            
if(sum == num):                                    
    print(num,"is an Armstrong Number.")          
else:
    print(num,"is not an Armstrong Number.")
 