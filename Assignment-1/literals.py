# Int Numeric Literal
a = 30
# Float Numeric Literal
b = 40.67
# Complex Numeric Literal
c = 10+4j
print(a)
print(b)
print(c)
print(c.real, c.imag)
string = 'Hello Guys'
multi_line = '''Hey
    There!!'''
char = 'Z'       
print(string)
print(multi_line)
print(char)
boolean1 = (1 == True)
boolean2 = (1 == False)
num = 20
age = 20
x = True + 10
y = False + 50

print(boolean1)
print(boolean2)

print(num==age)

print('Value of x:', x)
print('Value of y:', y)

soap = "Available"
handwash = None

def items(x):
    if x == soap:
        print('Soap:', soap)
    else:
        print('Soap:', handwash)

items(soap)
items(handwash)