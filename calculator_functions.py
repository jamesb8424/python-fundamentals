def add(num1, num2):
    return num1 + num2 


def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):

    if num2 == 0:
        print("You cannot divide by zero!")
    else:
        return num1 / num2


div(100,0)



print(add(1,2))


result = sub(10,3)
print(result)


result = mult(add(1,2), sub(10,3))
print(result)


