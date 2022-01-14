# Given a string and a non-negative int n,
# we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3.
# Return n copies of the front;


def front_times():
    print("Please enter a string:")
    string_input = str(input())
    if len(string_input) == 0:
        print("You\'ve enter an empty string")
        exit(0)
    print("Please enter a non-negative digit:")
    str_n = input()
    n = 0
    if str_n.isdigit() and int(str_n) >= 0:
        n += int(str_n)
    else:
        print("You\'ve enter not a non-negative digit")
        exit(0)
    if len(string_input) >= 3:
        string_output = string_input[:3] * n + string_input[3:]
    else:
        string_output = string_input * n
    print(string_output)


front_times()
