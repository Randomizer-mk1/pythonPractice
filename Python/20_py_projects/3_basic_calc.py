# define the function needed: add sub mul div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until user quits


def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")


def sub(a, b):
    answer = a - b
    print(a, "-", b, "=", answer + "\n")


def mul(a, b):
    answer = a * b

    print(a, "*", b, "=", answer + "\n")


def div(a, b):
    answer = a / b
    print(a, "/", b, "=", answer + "\n")


while True:
    print("A, addition")
    print("B, subtraction")
    print("C. multiplication")
    print("D. division")
    print("E. Exit")

    choice = input("Input your choice: ")
    choice = choice.lower()

    if choice == "a":
        print("addition")
        a = int(input("input first number"))
        b = int(input("input second number"))
        add(a, b)

    elif choice == "b":
        print("subtraction")
        a = int(input("input first number"))
        b = int(input("input second number"))
        sub(a, b)

    elif choice == "c":
        print("multiplication")
        a = int(input("input first number"))
        b = int(input("input second number"))
        mul(a, b)
    elif choice == "d":
        print("division")
        a = int(input("input first number"))
        b = int(input("input second number"))
        div(a, b)
    elif choice == "e":
        print("good bye")
        exit()
    else:
        print("\n", "Put only alphabet A from E")
        exit()
