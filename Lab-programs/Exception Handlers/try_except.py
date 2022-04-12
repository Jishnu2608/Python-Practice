'''If the Python program contains suspicious code that may throw the exception, 
we must place that code in the try block. The try block must be followed with the except statement, 
which contains a block of code that will be executed if there is some exception in the try block.'''

try:  
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b  
except:  
    print("Can't divide with zero")  