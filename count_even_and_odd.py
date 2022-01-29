def count_even_odd():
    a = input("Enter an integer: ")
    while len(a) == 0:
        a = input("Enter an integer: ")
    while a.isnumeric() is False:
        a = input("Enter an integer: ")
    a = int(a)
    even = 0
    odd = 0
    while a > 0:
        if (a % 10) % 2 == 0:
            even += (a % 10)
        else:
            odd += (a % 10)
        a = a // 10
    print(f"Sum of all even digits in number is {even}")
    print(f"Sum of all odd digits in number is {odd}")


count_even_odd()