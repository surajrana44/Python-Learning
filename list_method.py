 # ways to make list

#  1 square bracket 
my_list=[1,2,7,7.56,'hello',True]
print(my_list)

# 2 using list constructor

my_list=list((1,2,7,7.56,'hello',True))
print(my_list)

# update the list

lst=[1,2,3,4,5]
lst[2]='happy'
print(lst)
print(lst[2])

# using slicing 

lst=[1,2,3,4,5]
lst[0:4]=10,20,30,40
print(lst)

# repeting list

lst=[1,2,3,4,5]
print(lst*4)

# membership 


lst=[1,2,3,4,5,6,7,8,9]
number=int(input('enter your number: '))

if number in lst:
    print(f'found')
else:
    print(f'not found')

# copy in list 

list_1=[1,2,3,4,5,6]
list_2=list_1.copy() # copy is needed if i dont want changes in list_1

list_2[2]=2
print(list_1,list_2) 

## method of list 

# 1 append

a=[1,2,3,4,5]
a.append(6)  # 6 add hogayega awalys end me
print(a)

# 2 extend

a=[1,2,3,4]
b=[5,6,7]  
a.extend(b)  # a ke elements me b ke add hojayege
print(a)

# 3 insert

a=[1,2,3,4]
a.insert(0,"hello")
print(a)

# 4 remove 

a=[1,2,3,4]
a.remove(3)
print(a)

# 5 pop

a=[1,2,3,4]
popped=a.pop(0)
print(popped)
print(a)

# 6 clear 

a=[1,2,3,4]
a.clear()
print(a)

# 7 index

a=[1,2,3,4]
index=a.index(3)
print(index)

# 8 count 

a=[1,2,3,4,2,2,'java','hello']
count=a.count(2)
print(count)

# 9 sort 

a=[5,9,2,4,1,8,4,10,-1]
a.sort()
print(a)

# 10 reverse 

a=[5,9,2,4,1,8,4,10,-1]
a.reverse()
print(a)

# finiding minimun and maximum elements in list

a=[5,9,2,4,1,8,4,10,-1]
print(min(a))
print(max(a))

# finding common elements in list

a=[1,2,3]
b=[3,4,5]

s1=set(a)
s2=set(b)

s3=s1.intersection(s2)
print(list(s3))

# nested list

 
a=[1,2,3,4]
b=[7,8,a,'hello','jii']
print(b)

# range function

number=list(range(1,100,1))
'''
start=1
stop=100  # works only for integer
step=1
'''
print(number)

# list comprehension

squares=[i**2 for i in range(1,11) if i%2==0]
print(squares)