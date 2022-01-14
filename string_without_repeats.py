
def string_without_repeats():
    print('Please enter a string:')
    text1 = str(input())
    list1 = list(text1)
    list2 = [list1[0]]
    for i in list1:
        if i not in list2:
            list2.extend(i)
        else:
            continue
    text_output = ''.join(list2)
    print(text_output)


string_without_repeats()
