age = 22

# using conditional IF statement 
if age < 10:
    print("you are too young")

# using conditional ELIF statement
elif age >= 18 and age < 21:
    print("you can vote but not (legally) drink yet")

# using conditional ELSE statement
else:
    print("you ARE old enough")
# Nested conditionals
    if age >= 21 and age < 30:
        print("you dont know anything")
    else: 
        print("you know a few things")