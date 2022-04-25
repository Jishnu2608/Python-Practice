test_str = input("Enter string: ")

# initializing word list 
word_list = ["best", 'CS', 'for']
  
# initializing replace word 
repl_wrd = 'gfg'

res = ' '.join([repl_wrd if idx in word_list else idx for idx in test_str.split()])
  
# printing result 
print("String after multiple replace : " + str(res)) 