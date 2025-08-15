# learning by solving quetion

#question 1

for i in range(1,10,1):
    if i%2==0:
        print(f'even',i)
    else:
        print(f'odd',i)    
        
# question 2

start=int(input('enter start: '))
stop=int(input('enter stop: '))

if start>stop:
    print('invalid')
    quit()

skip=int(input('number you want to skip: '))

for i in range(start,stop):
    if i==skip:
        continue
    print(i)

# question 3

count=10

while count<=15:
    print(count)
    count+=1



