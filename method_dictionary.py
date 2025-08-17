## method

# 1 get 

profile={
    'nanme':'suraj', 'age': 22, 'salary': 120000
}

age=profile.get('age','not found')
print(age) 

# 2 keys

profile={
    'nanme':'suraj', 'age': 22, 'salary': 120000
}

key=profile.keys()
print(list(key))

# 3 value 

profile={
    'nanme':'suraj', 'age': 22, 'salary': 120000
}

values=profile.values()
print(list(values))

# 4 items 

profile={
    'nanme':'suraj', 'age': 22, 'salary': 120000
}

item=profile.items()
print(list(item))


# 5  pop

profile={
    'nanme':'suraj', 'age': 22, 'salary': 120000
}

popped=profile.pop('age','not found')
print(profile)

# 6 pop items

profile={
    'nanme':'suraj', 'age': 22, 'salary': 120000
}

popped=profile.popitem()
print(profile)

# 7 clear 

profile={
    'nanme':'suraj', 'age': 22, 'salary': 120000
}

clear=profile.clear()
print(profile)

# 8 dictionary comprehesnion

squares={x: x*x for x in range(1,11)}
print(squares)

# 9 nexted dict.....

language={
    'phyton': {'name': 'phyton', 'use case': ['ai','ml','web dev']},
    'java': {'name': 'java', 'use case': ['web dev']}
}

print(language)

# 10 loop

profile={
    'nanme':'suraj', 'age': 22, 'salary': 120000
}

for k in profile.values():
    print(k)
