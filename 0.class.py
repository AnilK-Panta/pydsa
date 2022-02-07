# This also works 
# class Computer:
#     def config():
#         print("I5, 10 Gen, 1TB")

# Computer.config()


# This is the actual way 
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