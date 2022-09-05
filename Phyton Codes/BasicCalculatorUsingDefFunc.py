def menu():
    print("""
    A. Addition
    B. Subtraction
    C. Multiplication
    D. Division
    E. Exit/quit
    """)


def add(x, y):
    answer = x + y
    print(f"The sum of {x} and {y} is {answer}")


def sub(x, y):
    answer = x - y
    print(f"The sum of {x} and {y} is {answer}")


def prod(x, y):
    answer = x * y
    print(f"The sum of {x} and {y} is {answer}")


def quot(x, y):
    answer = x / y
    print(f"The sum of {x} and {y} is {answer}")


while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "A" or choice == "a":
        print(" ADDITION")
        x = int(input("Enter first value: "))
        y = int(input("Enter first value: "))
        add(x, y)
    elif choice == "B" or choice == "b":
        print(" SUBTRACTION")
        x = int(input("Enter first value: "))
        y = int(input("Enter second value: "))
        sub(x, y)
    elif choice == "C" or choice == "c":
        print(" MULTIPLICATION")
        x = int(input("Enter first value: "))
        y = int(input("Enter second value: "))
        prod(x, y)
    elif choice == "D" or choice == "d":
        print(" Division")
        x = int(input("Enter first value: "))
        y = int(input("Enter second value: "))
        quot(x, y)
    elif choice == "E" or choice == "e":
        print(" Program Ended")
    else:
        print("Error")
