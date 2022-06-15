on = True


def addition():
    print("Addition:-")
    x = float(input("Enter your first number you want to input as value of x:"))
    y = float(input("Enter your second number you want to input as value of y:"))
    print(x + y)


def subtraction():
    print("subtraction:-")
    x = float(input("Enter your first number you want to input as value of x:"))
    y = float(input("Enter your second number you want to input as value of y:"))
    print(x - y)


def multiplication():
    print("multiplication:-")
    x = float(input("Enter your first number you want to input as value of x:"))
    y = float(input("Enter your second number you want to input as value of y:"))
    print(x * y)


def division():
    print("division:-")
    x = float(input("Enter your first number you want to input as value of x:"))
    y = float(input("Enter your second number you want to input as value of y:"))
    print(x / y)


while on:
    operation = input("Please choose any Operation from lists :- add , sub , mul & div or close")
    if operation == 'add':
        addition()

    elif operation == 'sub':
        subtraction()

    elif operation == 'mul':
        multiplication()

    elif operation == 'div':
        division()

    elif operation == 'close':
        on = False

    else:
        print("You have picked wrong input. Please try with correct input")


