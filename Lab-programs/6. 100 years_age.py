from datetime import datetime

name = input("Your name please: ")

age = int(input("Your present age: "))

hundred = int((100-age) + datetime.now().year)
print ('Hello %s. You are %s years old. You will turn 100 years old in %s.' % (name, age, hundred))
