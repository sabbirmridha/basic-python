try:
    digits =[40,0,20,]
    # outcome = digits[0] /digits [1]
    #outcome = digits[0]/digits[-1]
    outcome = digits[0]/digits[2]
    print(outcome)
    print("wow! you are almost there")

except ZeroDivisionError:
    print("Please try greater than zero")

except IndexError:
    print("Please pickup correct index")

except ValueError:
    print("Value Error")

finally:
    print("You are done")