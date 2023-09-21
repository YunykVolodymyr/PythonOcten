#Single line comment
'''
    Multiple
    lines
    comment
'''

#Prints into the console
#   sep -> (Separator), default=' '
#   end -> (After the output), default='\n'
print(1,2,3, sep=', ', end='end of the line\n')
# num =  int(input('Enter some number: '))
print(isinstance(3.3, float))

#Data types
i = 3     #int
f = 1.3   #float
b = False  #bool
s = 'text'#str
n = None  #NoneType

print(type(b))


#Types casting
int(False)
float('3 ')
bool(3)
str(n)


#Operators
3 + 3 # +=
5 - 3 # -=
2 * 2 # *=
3** 3 # **=
5 / 4 # /=
5// 2 # //=
7 % 5 # %=


#Logical operators
2 < 3
3 > 2
5 <= 3
6 >= 2
3 != 1 # 3 is 1
0 == 3 # 0 is not 3

# num = int(input('Enter a number: '));
# if num > 5:
#     print('yes')
# elif num > 3:
#     print('yes but actually no')
# else:
#     print('Nooooo')
#
# res = 'yes' if num > 10 else 'No';


#List
l = [1,2,3,4,5,6,7]
l2 = [23,34,54]
l[0]  # 1
l[-1] # 7
l[2] = 33
del l[3] # deletes by index
len(l) # length of the list
l.append(55) #adds to the end of the list
l.insert(-1, 0) # inserts object into specified index
l.pop(3) # deletes by index or the last element (Out of rage)
#l.remove(5) # removes by value first founnd
l += l2 # l.extend(l2)
l.index(6,2, 8) #finds index by value
l.count(3)
l.reverse()
l.sort(reverse=True)
l2 = l.copy()
l[1:5:-1]
print(l)


#Tuple
my_tuple = (1,2,3,4,6)


#Dictionary
dictionary = {
    'name': 'Max',
    'age': 4,
    'status': False
}
d = dict(asf=2, ink='blue')
dictionary['name']
dictionary['new_key'] = 'New value'
del dictionary['new_key']
dictionary.get('key', 'default value')
dictionary.items() # returns list of tuples key, value
dictionary.keys()  # returns list of keys
dictionary.pop('name') # returns value and deletes key and value
dictionary.popitem() # returns the last tuple and deletes it
dictionary.setdefault('key', 'value') # sets value to key if it's absent
dictionary.update({'another_dictionary_key': 'value'})
dictionary |= {'new_key': 'some value'}


#Set
l = [1,2,3,4,4,2]
set1 = {2, 3, 2}
s = set(l)
s.add(23)
s.issuperset(set1)
s.issubset(set1)
s.isdisjoint(set1)
s.union(set1)
s.intersection(set1)
s.symmetric_difference(set1)
s.remove(2)
s.discard(3)
s.pop() # returns and removes a random element of the set


#Strings
name = 'Illiia'
double_name = name * 2
sentence = 'Hi there {name} you are {age}'.format(name=name, age = 3)
sentence = f'Hi there {name} you are {3}'
name.index('ia') # index or error
name.find('hi') # index of -1
name.count('a')
name.capitalize()
name.upper()
name.lower()
name.title()
name.swapcase()
name.strip('l')
name.lstrip('I')
name.rstrip('a')
name.split('_')
name.partition('-')
name.islower()
name.isupper()
name.isalpha() # All are liters
name.isdigit()
name.isalnum() # liters or numbers
name.startswith('I')
name.endswith('a')
'separator'.join(['part1', 'part2'])
'  '.isspace()
name.replace('ll', 'd')
name[::2]


#Functions
min(1,2,4,-23)
max([2,3,4])
sorted([3,2,3], reverse=True) #Without affecting the original
pow(2,23)

def func_name(a, b, name='Olha', *args, **kwargs):
    print('Hello',a,b,name)
    print(args)
    print(kwargs)
    return


func_name(1,2, 'Vika', 2,3, reverse=True)


#Cycles

# i = 5
# while i > 0:
#     print(i)
#     i -= 1
#     if i == 2:
#         continue
# else:
#     print('next time')

l = [3,5,2,5]

for i, v in enumerate(l):
    print(v)

for i in range(0,5,2):
    print(i)

l = [i * 2 for i in range(10)]
print(l)