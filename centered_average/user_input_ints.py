def user_input_ints():
    print("Please enter a sequence of numbers")
    str_user = str(input())
    list_str = list(str_user)
    list_num = []
    for j in list_str:
        list_num.append(int(j))
    return list_num
