class Calculator:
    def __init__(self, inital_value):
        self.result = inital_value

    def add(self, num,):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    
    def mul(self, num):
        self.result *= num
        return self.result
    
    def div(self, num):
        self.result /= num
        return self.result

my_calculator = Calculator(0) # triggers the factory to make an object    
my_calculator.add(3)
my_calculator.add(4)
my_calculator.sub(5)



my_backup_calculator = Calculator(0)
my_backup_calculator.add(24)
my_backup_calculator.div(6)

print(my_calculator.result)
print(my_backup_calculator.result)


class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    
    def increment_age(self):
        self.age += 1

    def increment_weight(self):
        self.weight += 1

    def change_weight(self, new_weight):
        self.weight = new_weight

my_animal = Animal("Skeeter", 3, 15)
my_animal.increment_age()
for i in range(5):
    my_animal.increment_weight()

print(my_animal.weight)

        






