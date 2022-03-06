import array
salary = array.array('i',[15000,25000,30000,6000])
print(salary)
print("when index is 1:-")
print(salary[1])
print(salary[0:2])
# to insert elements-
salary.insert(0,200)
print(salary)

#modify elements
salary[2]=420
print(salary)
salary.remove(6000)
print(salary)

# array reverse
salary.reverse()
print(salary)

salary.pop(2)
print(salary)