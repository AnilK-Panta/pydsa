# This also works 
# class Computer:
#     def config():
#         print("I5, 10 Gen, 1TB")

# Computer.config()


# This is the actual way 
from pyexpat import model


class Computer:
    def config(self):  #Method (Function) with Attribute of self
        print("I5, 10 Gen, 1TB")

comp1=Computer()   #Creating object 1 of a class Computer
comp2=Computer()   #Creating object 2 of a class Computer

Computer.config(comp1)  #Calling method of a class of object 1
Computer.config(comp2)  #Calling method of a class of object 2

# The calling method is same for the below, which is actually seen in practice
comp1.config() #Takes comp1 as an Argument
comp2.config()

# __init__
class Car:
    def __init__(self, brand, release):
        self.b=brand
        self.r=release
    def config(self):
        print("Config is:", self.b, self.r)
model1=Car("Tesla", 5)
model2=Car("Hyundai", 10)

model1.config()
model2.config()


# comparing objects 
class Person:
    def __init__(self):
        self.name="Anil"
        self.age=25
    def Copmpare(self,others):
        if self.age==others.age:
            print("Both are of same age")
        else:
            print("Both are of different age")
    def Update(self):
        self.age=20

    
men1=Person()
men2=Person()
men1.Update()
men1.Copmpare(men2) #men1 passes as self and men2 passes as others in Compare(self, othere):
