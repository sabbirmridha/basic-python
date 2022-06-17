# Method overriding-

class Automation:
    def __init__(self):
        print("I am staying in Automation class")

#class Selenium(Automation):
    #pass  // just checking if i got the automation print function or not
#s =  Selenium()

class Selenium(Automation):
    def __init__(self):
        print("Overriding working and replacing the automation class print function : I am staying in Selenium")


s =  Selenium()
