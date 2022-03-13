file = open ("sabbir.txt","r")
# when line 2 print function will return true / false
# print(file.readable())
text = file.read()
# text = file.readlines() [0:2]
# text = file.readlines()   # this will show like list
print(text)

file.close()
