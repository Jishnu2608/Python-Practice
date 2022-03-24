import re
test_str = input("Enter string with HTML tags: ")
  
print("The original string is : " + str(test_str))
  
tag = input("Enter tag: ")
  
reg_str = "<" + tag + ">(.*?)</" + tag + ">"
res = re.findall(reg_str, test_str)

print("The Strings extracted : " + str(res))