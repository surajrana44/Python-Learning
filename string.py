
# ques 1

name='phyton'
print(name[-1])
print(name[0])

# quest 2

language='javascript'
for i in language:
    print(i)

# ques 3

password='123@phyton'
if len(password)>5:    # lenth of string finding fucntion (len)
    print(f'login succesfull')
else:
    print(f'lenth is too short or <5')

# " slicing in string "

text="phyton is the king of ai" 

print(text[2:7:1])  # string[start,stop,step]


# string.mehtod

## lower,upper method

str='this is phyton' # str='this is phyton'.upper() it is also right
print(str.upper()) 
print(str.lower())

## capitalise

str=input('enetr your name: ').capitalize()
print(str)
 
## title 

str=input('enetr your name: ').title()
print(str)

## replacing 

text='phyton is a programming langu...'
print(text.replace('phyton','java'))

