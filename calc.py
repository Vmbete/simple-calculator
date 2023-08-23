def add_two_integers(a, b):
    print(f"Adding {a} {b}")
    result = a + b
    print(f"Result: {result}")
    return result

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

add_two_integers(x, y)