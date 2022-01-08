print("Please input a string: ")
str_input = str(input())


def front3(string):
    if len(string) <= 3:
        return string * 3
    else:
        return string[:3] * 3


print(front3(str_input))
