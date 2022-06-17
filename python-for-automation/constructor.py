# Constructor-

class automation:


    def __init__(self,tools,id):
        self.tools = tools
        self.id = id

    def view(self):
        print(f"TooL's NAME : {self.tools}, TOOL ID : {self.id}")


tool1 = automation("Selenium" , 1)
tool1.view()

tool2= automation("Appium" ,2)
tool2.view()

