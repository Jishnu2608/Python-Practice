'''We can also use the else statement with the try-except statement in which, 
we can place the code which will be executed in the scenario if no exception occurs 
in the try block.'''
try:    
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b;    
    print("a/b = %d"%c)    
except:    
    print("can't divide by zero")    
else:    
    print("Hi I am else block")     