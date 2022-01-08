print("Please enter the first string")
a = str(input())
while len(a) == 0:
    print("Please enter the first non-empty string")
    a = str(input())
print("Please enter the second string")
b = str(input())
while len(b) == 0:
    print("Please enter the second non-empty string")
    b = str(input())


def make_abba(string1, string2):
    return string1 + string2 * 2 + string1


print(make_abba(a, b))
