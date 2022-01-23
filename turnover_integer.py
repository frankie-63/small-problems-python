print('Enter an integer')
x_str = str(input())
while len(x_str) == 0:
    print('Enter an integer')
    x_str = str(input())
while x_str.isnumeric() is False:
    print('Enter an integer')
    x_str = str(input())
x_list = list(x_str)
x_list.reverse()
output = int(''.join(x_list))
print(output)