# Inheritance
# ----
# we take the characteristics of a class to another class through inheritance .
# The main purpose of inheritance is to reuse the code.
# here , phone is parent class and Redmi is child class

# ---

class Phone: # parent class / super class / base class
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")


class Redmi(Phone): # Child class / sub class / Derived class
    # Call & message function will be also here because of inheritance
    def wifi(self):
        print("You can use wifi")


    def picture(self):
        print("You can take selfie")


#p = Phone()
#p.message()
#p.call()

r = Redmi()
r.wifi()
r.picture()
r.message()
r.call()
