import re

def CntSubstr(pattern, string):
  
    a = [m.start() for m in re.finditer(pattern, string)]
    return a
  
string = input("Enter string: ")
pattern = input("Enter pattern: ")

print(CntSubstr(pattern, string))