
# birthday reminder program using lists

import datetime
names = ["Ryan", "James", "Daniel"]
birthdays = ["06/01", "01/06", "01/06"]

today = datetime.datetime.today()
print(today)

today = str(today) # casting: force today to be a string

# convert 'today' variable into MM/DD
today = today.split()

today = today[0]
print("just the date: ", today)

today = today.split("-")
print("after split on - today: ", today)

today = today[1] + "/" + today[2]
print("today: ", today)


for ii in range(len(birthdays)):
    this_birthday = birthdays[ii]
    this_friend = names[ii]
    #print("ii, this_birthday, this_friend: ", ii, this_birthday, this_friend)

    if this_birthday == today:
        print("Wish " + this_friend + " a Happy Birthday")

        
