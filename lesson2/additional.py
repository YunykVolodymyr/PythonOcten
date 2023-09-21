# створити декоратор який буде рахувати кількість запущених функцій продекорованих цим декоратором

def make_decor():
    i = 0
    def inner(func):
        def inner_inner():
            nonlocal i
            i += 1
            print('count:', i)
            func()
            print('----------------')
        return inner_inner
    return inner


decor = make_decor()

@decor
def func1():
    print('func1')

@decor
def func2():
    print('func2')

func1()
func1()
func2()
func1()

# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
def show_fibonacci(x: int):
    res = [1,1]
    for i in range(x - 2):
        res.append(res[-1] + res[-2])
    print(res[:x])

print('*' * 50)
show_fibonacci(10)
show_fibonacci(1)
# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3
def odd_n_even(n: int):
    l = len([i for i in str(n) if int(i) % 2 == 0])
    print(f'п = {l}, н = {len(str(n)) - l}')

print('*' * 50)
odd_n_even(225688)
odd_n_even(33294)

# прога, що виводить кількість кожного символа з введеної строки, наприклад: st = 'as 23 fdfdg544'
# введена строка
#
# 'a' -> 1  # вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1

def count_chars(s: str):
    return '\n'.join([f'\'{c}\' -> {s.count(c)}' for c in set(s)])

print('*' * 50)
print(count_chars('as 23 fdfdg544'))

# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:
#
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]

def generate_odd(n: int):
    l = range(1,n + 1, 2)
    n = 1
    res = []
    temp = []
    for i in l:
        if len(temp) < n:
            temp.append(i)
        else:
            n += 1
            res.append(temp)
            temp = [i]
    res.append(temp)
    return res
print('*' * 50)
print(generate_odd(19))
print(generate_odd(11))
print(generate_odd(9))
print(generate_odd(13))


# найти со списка только уникальные числа
#
# пример [1,2,3,4,2,5,1] => [ 3, 4, 5 ]

def find_unique(l):
    return [i for i in l if l.count(i) == 1]

print('*' * 50)
print(find_unique([1,2,3,4,2,5,1]))