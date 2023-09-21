def last_digit(lst):
    if len(lst) == 0:
        return 1
    n = lst[-1]
    for i in range(1, len(lst) ):
       n = pow((lst[-i - 1] ), n % 4 + 4 if n > 3  else n  )
    return n % 10

def last_digit(lst):
    lst.reverse()


print(last_digit([4, 3, 6]))