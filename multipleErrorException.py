try:
    var1=int(input("Input your first variable:"))
    var2=int(input("Input your second variable:"))
    outcome = var1//var2
    print(outcome)

except (ValueError,ZeroDivisionError):
    print("Please provide correct input")


finally:
    print("Thank you for  trying")