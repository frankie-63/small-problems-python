from user_input_ints import user_input_ints
from input_output_decor_ints import output_decor


@output_decor
def count_evens(list1):
    count = 0
    for i in list1:
        if i % 2 == 0:
            count += i
    print(count)
    return count


print("Please enter a sequence of numbers:")
count_evens(user_input_ints())
