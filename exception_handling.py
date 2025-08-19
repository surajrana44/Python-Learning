
# exception handling 

''' 
1 try-except
try: code that may raise an exception/error
except: code that runs if an exception occurs

2 finally: code that runs no matter what, even if an exception occurs

3 nested try-except
4 raise: used to raise an exception manually
5 custom exception: creating your own exception class

'''
# example of exception handling

try:
    num=int(input("Enter a number: "))
    result = 10 / num
    print(f'result is {result}')

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

finally:
    print(f'Execution completed. Thank you!')

# nested try-except example

try:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    try:
        result= num1 / num2
        print(f'Result is {result}')
    except ZeroDivisionError:
        print("Error: You cannot divide by zero .")
except ValueError:
        print("Error: Invalid input. Please enter a valid number.")

# check passowrd strength example

def check_password(password):
     if len(password) <8:
         raise Exception("Password must be at least >=8 characters long.") # custom exception

     print("Password is strong enough.")   
try:
    password = input("Enter your password: ")
    check_password(password)

except Exception as e:
   print('error',e)