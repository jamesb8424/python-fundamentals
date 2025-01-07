import random

Num= random.random() * 100
Num= int(Num)
print(Num)
if Num%2 == 1:
    print("Weird 1")
else:
    if Num >=2 and Num <=5:
        print("Not Weird")

    if Num >=6 and Num <=20:
        print("Weird 2")

    if Num >20:
        print("Not Weird 3")
