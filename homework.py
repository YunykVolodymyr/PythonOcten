# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# s = input('Enter a string: ')
# print(*[c for c in s if c.isdigit()], sep=', ')

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
# st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# s = input('Enter a string: ') + ' ';
# temp = ''
# res = []
# s += ' '
# for i in s:
#     if i.isdigit():
#         temp += i
#         continue
#     elif temp != '':
#         res.append(temp)
#         temp = ''
# print(*res, sep=', ')
# #################################################################################
#
# list comprehension
#
# 1)є строка:
greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# print([i.upper() for i in greeting])

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([i ** 2 for i in range(50) if i % 2 != 0])


# function
#
# - створити функцію яка виводить ліст
def show_list(l):
    print(l)


# show_list([1, 2, 3])


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def max_number(a, b, c):
    m = max(a, b, c)
    print('Max number:', m)
    return m


# print('Max number:', max_number(3, 5, 2))


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def min_and_max(*args):
    print('Max arg:', max(args))
    return min(args)


# print('Min arg:', min_and_max(2, 3, 5, -3, 55))


# - створити функцію яка повертає найбільше число з ліста
def max_in_list(l):
    return max(l)


# print('Max in the list:', max_in_list([2, 3, 55]))


# - створити функцію яка повертає найменьше число з ліста
def min_in_list(l):
    return min(l)


# print('Min in the list:', min_in_list([2, 3, -2]))


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def add_values_of_list(l):
    sum = 0
    for i in l:
        sum += i
    return sum


# print('Sum:', add_values_of_list([2, 3, 5]))


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def mean(l):
    sum = 0
    for i in l:
        sum += i
    return sum / len(l)


# print('Mean:', mean([1, 2, 3]))
#
#
#
#
# ################################################################################################
# 1)Дан list:
l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


#   - знайти мін число
def find_min(l):
    print(l)
    print('Min:', min(l))


#   - видалити усі дублікати
def remove_duplicates(l):
    print(l)
    print('Duplicates removed:', [v for i, v in enumerate(l) if l.index(v) == i])


#   - замінити кожне 4-те значення на 'X'
def replace_every_fourth(l):
    print(l)
    print('Replaced:', ['X' if (i + 1) % 4 == 0 else v for i, v in enumerate(l)])


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def print_square(a):
    print(('*' * a) + '\n' + ('*' + (' ' * (a - 2)) + '*\n') * (a - 2) + '*' * (a if a > 1 else 0))


# 3) вывести табличку множення за допомогою цикла while
def print_table():
    i = j = 1
    while i < 10:
        s = ''
        while j < 10:
            s += str(i * j).ljust(3)
            j += 1
        print(s)
        i += 1
        j = 1


# 4) переробити це завдання під меню

while True:
    l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print('1.Знайти мін число')
    print('2.Видалити усі дублікати')
    print('3.Замінити кожне 4-те значення на \'X\'')
    print('4.Вивести на екран пустий квадрат з "*"')
    print('5.Вывести табличку множення')
    print('6.Вихід')
    n = input('Ваш вибір: ')
    if n == '1':
        find_min(l)
    elif n == '2':
        remove_duplicates(l)
    elif n == '3':
        replace_every_fourth(l)
    elif n == '4':
        print_square(int(input('Введіть сторону квадрата (ціле число):')))
    elif n == '5':
        print_table()
    elif n == '6':
        break
    else:
        print('Введіть цифру 1-6')
