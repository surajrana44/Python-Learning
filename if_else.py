# explaining by example the use case of if,elif,else 

# Question 1

age=int(input('enter you age: ')) 

if (age>=18 and age<=100):
     print('you can vote')
elif (age<=0 or age>100):
     print('invalid')
else:
     print('you are not eligible for vote')

# Question 2

num_1=float(input('enter your no 1 = '))
num_2=float(input('enter your no 2 = '))

choice=input('enter your choice + - * = ')

if choice=='+':
    print(f'Addition: {num_1 + num_2}')
elif choice=='-':
    print(f'subtraction: {num_1-num_2}')
elif choice=='*':
     print(f'multiply: {num_1*num_2}')
else:
    print(f'invalid choice')