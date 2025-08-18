'''
1- classes & objects
2- inheritance
3- encapsulation
4- abstraction
5- polymorphism

'''

# clases & objects  

class car(): # blueprint
    #method/property
    def start(self):
        print(f'car is starting.......')
    def stop(self):
        print(f'car is stop.......')

car1=car()  # object
car2=car()

car1.start()
car1.stop()

car2.start()
car2.stop()

# example 2

class car():
    def set_deatils(self,brand,color):
        self.brand=brand
        self.color=color
    def show_details(self):
        print(f'this car is a {self.color} {self.brand}')

car1=car()
car1.set_deatils('tesla','red')

car2=car()
car2.set_deatils('bmw','black')

car1.show_details()
car2.show_details()

# constructor

'''
__init__(self)

'''

# without constructor

class car():
    def set_deatils(self,brand,color):
        self.brand=brand
        self.color=color

car1=car()
car1.set_deatils('tesla','red')

print(car1.brand)
print(car1.color)

# with constructor

class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

car1 = Car('tesla','red') # value automatically set without calling set_deatils property
print(car1.brand,car1.color)

'''
syntax :
class car:
    def __init__(self,parameter1,para2,para2):
      self.property1=parameter1
      self.property2=parameter2

      
types of constructor
1. default constructor (self)
2. parameterized constructor (self,name,age,marks etc)
3.constructor with default value (self, name='unkown',age=0 etc)

'''