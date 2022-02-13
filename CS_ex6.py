a = float(input("Enter the first floating-point number: "))
b = float(input("Enter the second floating-point number: "))
if round(a, 3) == round(b, 3):
    print(f"{a} and {b} are equal")
else:
    print(f"{a} and {b} are different")
