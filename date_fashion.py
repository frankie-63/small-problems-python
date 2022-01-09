import random

you = random.randint(0, 10)
date = random.randint(0, 10)
print("The stylishness of your clothes is ", you)
print("The stylishness of your date's clothes is ", date)


def date_fashion(a, b):
    if a >= 8 or b >= 8:
        return 2
    elif a <= 2 or b <= 2:
        return 0
    else:
        return 1


print("The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes.")
print("Today the result is ", date_fashion(you, date))
