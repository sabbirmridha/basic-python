digits =[1,2,3,4,5,6,7]

# Return true
print( 7 in digits)

# return False
print( 17 in digits)

digits.append(8)
print(digits)

#insert at position
digits.insert(0,9)
print(digits)

#remove digit
digits.remove(9)
print(digits)


# clear all digits
digits.clear()
print(digits)