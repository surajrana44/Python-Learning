 # basic function syntax 

# 1 square root of number solving by using funtion
def square_of_num(number):
    return (number ** 2)

result=square_of_num(4)
print(result)
print(square_of_num(5))

# 2 function with multiple parameter

def add(num1,num2):
    return num1 + num2

result=add(6,6)
print(result)
print(add(6,6))

# 3 function returning multiple values

import math

def circle_stats(radius):
    area =  math.pi * radius ** 2
    cicumfrence = 2 * math.pi * radius ** 2
    return area, cicumfrence

a,c = circle_stats(4)
print("area: ", a , "circumfrence: ", c)

# 4 function with default parameter

def greet(name= "jii"):
    return f' hello, {name} !'

print(greet())

# 5 by using lamda function we are solving cube of number

cube = lambda x: x ** 3

print(cube(3))

# 6 function with *args

def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1,2,3))

# 7 function with **kwargs

def print_info(**kwargs):
   for key,value in kwargs.items():
       print(f'{key}: {value}')
       
       

print_info(name='superman', power='flying', move='strongh punch')

# 8 yield keyword in function

def generate_even_numbers(n):
    yield from range(2, n + 1, 2)

for num in generate_even_numbers(10):
    print(num)

