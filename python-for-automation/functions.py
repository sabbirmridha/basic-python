# Functions -
def calculation():
    # fixed input -

    # x = 30
    # y = 50
    # z = 2

    # taking input using prompt -

    x = int(input("Enter the value of x :"))
    y = int(input("Enter the value of y :"))
    z = int(input("Enter the value of z:"))

    print("Here is your desired calculation:")
    
    print(x+y)
    print(y-x)
    print(int(y/2)) # type casting to integer value
    print(x*2)

calculation()