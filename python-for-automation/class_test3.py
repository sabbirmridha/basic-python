# use of methods in class & set value in a function

class students:
    name = " "
    id = " "
    cgpa = " "

    def set_value(self,name,id,cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa


    def show(self):
        print(f"NAME : {self.name} , ID: {self.id} , CGPA : {self.cgpa} ")



student1 = students()

student1.set_value("Mridha","15-47895-1",3.5)
student1.show() # calling show function  to show name , id & cgpa

# print(f"NAME : {student1.name} , ID : {student1.id} , CGPA : {student1.cgpa}")

student2 = students()
student2.set_value("Test","7894562",3.1)
student2.show()




