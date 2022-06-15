# def employee_info(name, experience, designation):
# trying with keyword argument-
def employee_info(name, experience =1 ,designation="Software Automation Engineer "):

    print("{} has {} years of expertise with {} field " .format(name,experience,designation))

#  Try using expected value-
employee_info("Sabbir", 2 , "Software Engineer QA")

#trying for keyword argument-
employee_info("S.Mridha")
# replacing value-
employee_info(experience=0 ,name="sabbir" , designation="Accounting")




