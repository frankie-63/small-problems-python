print('Please enter an integer')
n = int(input())


def diff21(i):
    if i <= 21:
        return 21 - i
    else:
        return (i - 21) * 2


print(diff21(n)) # some comments
