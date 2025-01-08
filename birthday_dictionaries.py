import datetime


data = {
    "names": ["Ryan", "James", "Brian", "Justin"],
    "birthdays": ["01/27", "01/06", "02/22", "05/01"]
}

today = datetime.datetime.today()
print("today: ", today)


today =str(today)
today = today.replace("-", "/")
today = today.split()
today = today[0]
today = today[5:]
print(today)


for ii in range(len(data["names"])):
    this_birthday = data["birthdays"][ii]
    this_friend= data["names"][ii]

    if this_birthday == today:
        print("Wish " + this_friend + " a Happy Birthday!")
