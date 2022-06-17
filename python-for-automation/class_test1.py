# CLASS-
class employee:
    name = " "
    designation = " "
    salary = " "

Sabbir = employee()

# print(isinstance(Sabbir,employee)) # ---> this will insure me that if Sabbir is really a object of employee class

Sabbir.designation = "Test Automation Engineer"
Sabbir.salary = 60000

print(f"Designation : {Sabbir.designation} , SALARY : {Sabbir.salary}")


Mridha = employee()

Mridha.designation = "SQAE"
Mridha.salary = 40000
print(f"Designation : {Mridha.designation} , Salary : {Mridha.salary}")
