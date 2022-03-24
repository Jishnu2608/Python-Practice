import re

regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
     
def check(string):
 
    if(re.search(regex, string)):
        print("Status: Valid")
    else:
        print("Status: Invalid")
     
if __name__ == '__main__' :

    string = input("Enter string to be checked: ")
    check(string)