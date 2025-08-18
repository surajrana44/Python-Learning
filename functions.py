
# greet is function name
def greet():
    print('hi')

greet()

# parameter of fuction

def greet(name): # name - parameter
    print('hi',name)

greet('suraj') # suraj - arguement

# arguement is 3 types 

#1 postion arguement

def greet(name,city):
    print(f'welcome {name} to the {city}')

greet('mumbai','raju')

# 2 keyword arguement

def greet(name,city):
    print(f'welcome {name} to the {city}')

greet(city='mumbai',name='raju') 

# 3 defualt arguement 

 
def greet(name='suraj',city='mumbai'):
    print(f'welcome {name} to the {city}')

greet()

# return function  

def full_name(first_name,last_name):
    full_name=f'{first_name} {last_name}'
    return full_name

name=full_name('suraj','rana') 
print(name)   

# local variable

def msg():
    my_msg="go all out" # my_msg is local variable issi function me chalega bahar nhi
    return my_msg

mail=msg()
print(mail)

# global variable

def msg():
    print('inside the function',choice)

choice='i love phyton' # choice is global variable koe bhi acess kar sakta h

msg()

# decorator

# main function ko change kar bina additional functionality/function add kar de it is called decorator

def my_decorator(func):
    def wrapper():
        print("something is happening before the function is called")
        func()
        print("something is happening after the function is called")
    return wrapper
@my_decorator
def say_hello():
    print("hello")

say_hello()

# generator 

# yield keyword

def count_down(num):
    while num>0:
        yield num # yeild values one at a time
        num-=1 # ek baar me ek value per operate karte ha

# using generator

for num in count_down(10):
    print(num)

























