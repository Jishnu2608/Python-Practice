x="Variable-1"      #assign variable
y=10        #assign variable
def func():
    print("Access from function: " + x,",", y+11)

func()
print("Access from outside function: "+x,",", y+3)
