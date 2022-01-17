from user_input_ints import user_input_ints
from input_output_decor_ints import output_decor


@output_decor
def centered_average(list_of_ints):
    list_of_ints.sort()
    list_of_ints.pop(0)
    list_of_ints.pop(-1)
    len_loi = len(list_of_ints)
    count = 0
    for i in list_of_ints:
        count += i
    x = int(count / len_loi)
    print(x)
    return x


centered_average(user_input_ints())
print("For list -10, -4, -2, -4, -2, 0")
centered_average([-10, -4, -2, -4, -2, ])
