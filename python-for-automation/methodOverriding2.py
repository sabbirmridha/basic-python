# Method overriding & how to use super keyword and super class constructor-

class Automation:
    def __init__(self):
        print("I am staying in Automation class")

#class Selenium(Automation):
    #pass  // just checking if i got the automation print function or not
#s =  Selenium()

class Selenium(Automation):
    def __init__(self):
        super().__init__()  # we can use super class property using this line
        print("Overriding working and replacing the automation class print function : I am staying in Selenium")


s =  Selenium()
