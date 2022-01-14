# Given 3 int values, a b c, return their sum.
# However, if one of the values is the same as another of the values, it does not count towards the sum.


def lone_sum(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    if my_list[0] == my_list[1] == my_list[2]:
        sum_abc = 0
    elif my_list[0] == my_list[1]:
        sum_abc = my_list[2]
    elif my_list[1] == my_list[2]:
        sum_abc = my_list[0]
    else:
        sum_abc = a + b + c
    return sum_abc


print(lone_sum(1, 2, 3))  # 6
print(lone_sum(3, 2, 3))  # 2
print(lone_sum(3, 3, 3))  # 0


