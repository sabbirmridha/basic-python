# use of methods in class
class students:
    name = " "
    id = " "
    cgpa = " "

    def show(self):
        print(f"NAME : {self.name} , ID: {self.id} , CGPA : {self.cgpa} ")



student1 = students()

student1.name = "Sabbir"
student1.id = "180-548682-7"
student1.cgpa = "3.80"
student1.show() # calling show function  to show name , id & cgpa

# print(f"NAME : {student1.name} , ID : {student1.id} , CGPA : {student1.cgpa}")

