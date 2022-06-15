# if -elif

day = input("Select the day from list : Friday , Saturday , Sunday , Monday ,Tuesday , Wednesday , Thursday:-")
if day == "Friday":
     print("Today is your Holiday because today is {}".format(day))
elif day == "Saturday":
     print("Today is holiday because today is {}".format(day))
elif day == "" :
     print("You have entered empty string . Can you Please pick a day from list?")



else:
    print("Today is {} & Office is open . ".format(day))



