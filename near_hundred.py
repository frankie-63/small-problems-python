print('Please enter an integer')
n = int(input())


def near_hundred(i):
    if 100 - 10 <= i <= 100 + 10 or 200 - 10 <= i <= 200 + 10:
        return True
    else:
        return False


print(near_hundred(n))
