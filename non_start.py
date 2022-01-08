print("Please enter the first string")
str1 = str(input())
while len(str1) == 0:
    print("Please enter the first non-empty string")
    str1 = str(input())
print("Please enter the second string")
str2 = str(input())
while len(str2) == 0:
    print("Please enter the second non-empty string")
    str2 = str(input())


def non_start(string1, string2):
    return string1[1:] + string2[1:]


print(non_start(str1, str2))
