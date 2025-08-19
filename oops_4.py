# Inheritance

# example of inheritance in Python

class animal: # parent class
    def speak(self):
        print("Animal speaks")

class dog(animal): # dog inherits from animal , child class inherit from parents
    def bark(self):
        print('dogs barks')

Dog = dog()
Dog.speak()
Dog.bark()

# abtraction

from abc import ABC,abstractmethod

class vehicle(ABC): # abstract class unnessary details ko hide karta ha, acts as a blueprint/ child class must implement the abstract class
    @abstractmethod
    def start(self):
        pass # no implementation here

class car (vehicle): # child class
        def start(self):
            print('car is starting')
    
class bike (vehicle): # child class
        def start(self):
            print('bike is starting')

bmw= car()
hero=bike()

bmw.start()
hero.start()