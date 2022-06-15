# Contunue , pass
print("Continue:")
for digits in range(1,15):
    if digits == 5:
       print("Hello 5 has skiped")
       continue


    print("The digit is {}".format(digits))

# Pass-
print("PASS:")
for digits in range(1,6):
    if digits ==4:
        pass
    else:
        print("Your digit is {}".format(digits))

