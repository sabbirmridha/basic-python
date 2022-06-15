# While loop & use of break

score_n =80
while score_n > 33 :
    print("You are a certified test engineer. your score is {}".format(score_n))
    score_n = score_n -1
    if score_n == 60:
        break   # use of break after showing 61 loop will break

        