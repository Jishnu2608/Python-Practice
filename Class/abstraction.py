from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def age(self):
        pass

class Infact(User):
    def age(self):
        print("I am 6 years old")
class Teenage(User):
    def age(self):
        print("I am 20 years old")
class Adult(User):
    def age(self):
        print("I am 35 years old")
class Old_age(User):
    def age(self):
        print("I am 60 years old")

#driver code
A=Infact()
A.age()

A=Teenage()
A.age()

A=Adult()
A.age()

A=Old_age()
A.age()