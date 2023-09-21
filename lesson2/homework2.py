# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання
from typing import Callable
def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:

    things_to_do = []

    def add_todo(assignment: str) -> None:
        things_to_do.append(assignment)

    def get_all() -> list[str]:
        return things_to_do.copy()

    return (add_todo, get_all)

add, read = notebook()
add('fed the cat')
add('do the dishes')
l = read()
l.append('hi')
print(l)
print(read())

#3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(num):
    return [str(v).ljust(len(str(num)) - i, '0') for i,v in enumerate(str(num)) if v != '0']


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована
# цим декоратором, та буде виводити це значення після виконання функцій

def decor(func):
    i = 0
    def inner():
        func()
        nonlocal i
        i += 1
        print(f'Executed {i} times')

    return inner


@decor
def fun():
    print('Hello world')


fun()
fun()
fun()
fun()