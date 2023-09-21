#Destructurisation ////////////////////////////////////

l = [1,2,3,4,5,6]
a, *_, b = l # a == 1, b == 6, _ == [2-5]

d = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
}

def p(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

p(*d)


#Decorator ////////////////////////////////////////////////


def decor1(func):
    def inner(*args):
        print('*' * 20)
        func(*args)
        print('*' * 20)

    return inner

@decor1
@decor1
def greeting(name, age):
    print(f'Hello, {name} -- {age}')

# second = decor1(greeting)
# second('Oleh', 13)

greeting('Oleh', 22)

#Scope //////////////////////////////////////////////////////

print(globals())
print(locals())

for i in range(5):
    print(i)

print(i) # 4 because of global scope

name = 'max'
def func():
    #global name - makes the function work with name of global scope
    name = 'ivan'
    print(name) # ivan because of local scope

func()
print(name) # max because of global scope

#nonlocal ///////////////

def a():

    name = "Vitya"

    def b():
        nonlocal name
        name = "Peter"
        print(name)

    b()
    print(name)

a()

def counter():
    x = 0

    def inner():
        nonlocal x
        x += 1
        print(x)

    return inner

count1 = counter()
count2 = counter()

count1()
count1()
count2()
count1()
count2()


#Lambda ////////////////////////////////////////////////////////

func = lambda x, y: x + y

print(func(1, 2))

people = [
    {'name': 'Ivan', 'age': 23},
    {'name': 'Alina', 'age': 13},
    {'name': 'Nina', 'age': 26},
    {'name': 'Taras', 'age': 25},
]

people.sort(key=lambda person: person['name'], reverse=True)
print(people)

print(list( map(lambda person: person['name'], people)))
print(list(filter(lambda person: person['age'] > 23, people)))

# Type annotation ////////////////////////////////////
def a(name: str) -> None:
    print(name.find('a'))

a('Halya')

from typing import TypedDict

User = TypedDict('User', {'name': str, 'age': int})

user:User = {'name': 'Max'}