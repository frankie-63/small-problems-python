print("Please enter a string")
a = str(input())
while len(a) == 0:
    print("Please enter a non-empty string")
    a = str(input())


lst = []
i = 0
while i < len(a):
    lst.extend(a[i])
    i += 1


lst2 = []
for j in lst:
    lst2.extend(j * 2)


a2 = ''.join(lst2)
print(a2)