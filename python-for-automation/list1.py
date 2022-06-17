designation = ["Project Manger", "Web Developer" , "SQA Engineer"]
salary =[70000, 60000, 50000]
experience =[5.5, 3, 2, 1]
employee =["Sabbir","Mridha", "Robin", "Akib"]


digits = [1011 ,1012, 1028 ,1005]

print(designation,salary)
print(designation,experience)

# adding a single item in  designation list-
# append
designation.append("Business Analyst")
print("newly added designation for append: ", designation)

# extend -
designation.extend(salary) # this extend method will merge two list in a one list
print("here is effect for using extend: ", designation)

# Remove-
print("Current designation lists:-",designation)
designation.remove("Business Analyst")
print("Here is the list of designation after using remove:" , designation)

# pop-
print("printing employee:-", employee)
employee.pop(0)
print("doing pop(0) on employee",employee)

print("printing employee:-", employee)
employee.pop(2)
print("doing pop(2) on employee",employee)

print("printing employee:-", employee)
employee.pop(-1)
print("doing pop(-1) on employee",employee)

# sort- this will sort the items -

print("the digits are:-", digits)
digits.sort()
print("The sorted digits are-",digits)

# To check a large datasets- this will show result as True or False-

print("TO check if 5 is in digits list or not :",5 in digits)
print("TO check if 1028 is in digits list or not :",1028 in digits)

# count function- this will count how many times the parameter value has in the lists-
print(digits.count(1028))
print("printing digits", digits)
print("printing the index of digit:",digits.index(1028))


