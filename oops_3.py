'''
polymorphism - (one name , many forms ) simple defination

ex- run
.person can run
.computer can run
.car can run etc 

'''


# polymorphism with classes method overinding

class bird():
    def sound (self):
        print('birds can make sweet noice')
    
class crow(bird):
     def sound(self):
        print('crow cannot make sweet noice')
class parrot(bird):
     def sound(self):
        print('parrot can make sweet noice')

animal1=crow()
animal2=parrot()

animal1.sound()
animal2.sound()

'''
encapsulation - 1. private deatils class ki hide karta ha 
                2. private attributes directly access nhi kar sakte 
                
                
'''

# example 1

class Bankaccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.__balance= balance  # private variable ban gaya balance / agar .balance karta toh public hojata

    def deposit(self,amount=000):
        self.__balance+=amount
        print(f'desposited {amount} and new balance {self.__balance}')

    def get_balance(self):
        return self.__balance # controlled access

account=Bankaccount('1234',4000)

account.deposit(2000)
print(account.get_balance())