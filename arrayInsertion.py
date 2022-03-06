bug =[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

bug.insert(3,[90,91,92,93,94])
print(bug)


#update array element
bug[-1][3]=1001
print(bug)

del bug[-1]
print(bug)
# geting the length of the array-
print(len(bug))