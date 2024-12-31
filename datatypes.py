print(type(7)) # will be an "int"
print(type("my name is James")) # will be a "str"
print(type([1,2, "hi"])) # will be a "list"

mylist = [1,2, "hi"] # 0 index=1, 1 index=2, 3 index="hi"

print(type(mylist[0])) # will be an "int"
print(type(mylist[2])) # will be a "str"

age = 40

print("type of my age as an integer: ", type(age)) # Should be an "int"

# changing age to a string
age = str(age)

print("type of my age as a string: ", type(age)) # Should be a "str"


burger = 3.45
print(type(burger)) # Should be a "float"

# add the "int" type to allow for division, but still keeping (age) as a string
half_my_age = int(age) / 2
print(half_my_age) # type(half_my_age)) would still be a "float"


xy_coordinate = (21, -4)
print(type(xy_coordinate)) # Should be a "tuple"

dictionary = {"age": 31, "height_in_inches": 66, 4: "another number"}
print(dictionary)
print(list(dictionary.keys()))
print(list(dictionary.values()))

print(type(dictionary))
print(type(list(dictionary.keys())))

print(type(list(dictionary.keys())[0]))
print(type(list(dictionary.keys())[2]))









