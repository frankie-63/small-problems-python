print("Please enter a string")
a = str(input())
while len(a) == 0:
    print("Please enter a non-empty string")
    a = str(input())


def xyz_there(string):
    v = list(string.lower())
    if v.__contains__('.'):
        w = list()
        w += v[0:v.index('.')]
        if w.__contains__('x' and 'y' and 'z'):
            if w.index('x') == w.index('y') - 1 == w.index('z') - 2:
                return True
            else:
                return False
        else:
            return False
    else:
        if v.__contains__('x' and 'y' and 'z'):
            if v.index('x') == v.index('y') - 1 == v.index('z') - 2:
                return True
            else:
                return False
        else:
            return False


print(xyz_there(a))
