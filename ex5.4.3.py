str_in = input()
str1 = str_in.replace(' ', '')
lst = list(str1)
lst.append('end')
lst.insert(0, '+')
lst1 = []
summ = 0
d1 = 0
d2 = 0
i = 1
for j in range(i, len(lst)):
    if lst[j] == '+' or lst[j] == '-':
        lst1 = lst[i:j]
        lst1sum = []
        a = len(lst1) - 1
        count = 0
        while a > -1:
            lst1sum.append(int(lst1[a]) * int(str('1' + '0' * count)))
            a -= 1
            count += 1
        d1 = sum(lst1sum)
        lst1 = []
        if lst[i - 1] == '+':
            summ += d1
        elif lst[i - 1] == '-':
            summ -= d1
        d1 = 0
        j += 1
        i = j
    elif lst[j] == 'end':
        lst1 = lst[i:j]
        lst1sum = []
        a = len(lst1) - 1
        count = 0
        while a > -1:
            lst1sum.append(int(lst1[a]) * int(str('1' + '0' * count)))
            a -= 1
            count += 1
        d1 = sum(lst1sum)
        lst1 = []
        if lst[i - 1] == '+':
            summ += d1
        elif lst[i - 1] == '-':
            summ -= d1
        break

print(summ)



