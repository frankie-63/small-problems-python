def array123(list):
    list_num = []
    for j in list:
        list_num.append(int(j))
    i = 0
    while i < len(list_num) - 2:
        if list_num[i] == 1:
            if list_num[i+1] == 2:
                if list_num[i+2] == 3:
                    return True
                else:
                    i += 1
                    continue
            else:
                i += 1
                continue
        else:
            i += 1
            continue
    return False


print("The program will return True if the row contains a sequence 123, otherwise it will return False")
print("Please enter a row of numbers, for example: 5638 or 394312345")
list_input = list(input())
print(array123(list_input))
