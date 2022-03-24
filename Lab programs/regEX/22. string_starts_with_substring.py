import re

def find(string, sample) :

  if (sample in string):
  
      y = "\A" + sample
  
      x = re.search(y, string)
  
      if x :
          print("String starts with the given substring")
  
      else :
          print("String doesn't start with the given substring")
  
  else :
      print("Entered string isn't a substring")
  
  
string = input("Enter string: ")
sample = input("Enter sample: ")

find(string, sample)
  
