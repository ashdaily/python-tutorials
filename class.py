# class 
# anything related to real world
# For example: Students, Teachers, School,  Cars, 
# Person, Rocket, Motorcycle
class Person:
    # class has two components
    # 1. Variables
    # 2. Functions
    is_human = True
    planet = "Earth"

    def __init__(self, first_name,last_name, nickname, speed):
        # instantiates when a object is created
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.speed = speed

    def full_name(self): #first argument will always be self
        return self.first_name + self.last_name # need self to access the class variables

    def get_profile(self):
        return {
            "first_name" : self.first_name,
            "last_name": self.last_name,
            "nickname" : self.nickname
        }

    def greets(self):
        return f"{self.nickname} says hello!!"
        
    def check_if_slow_or_fast(self):
        if self.speed > 10:
            return f"{self.nickname} is running fast, at {self.speed} kmph"
        else:
            return f"{self.nickname} is running slow, at {self.speed} kmph"

    def is_nickname_long(self):
        if len(self.nickname) > 5:
            return True
        else:
            return False

# object is type of a class
# obj = ClassName()

amy = Person("amit", "deshwal", "amy", 10)
amy.first_name #amit
amy.last_name # deshwal
amy.nickname # amy

archie = Person("shaurya", "katoch", "archie", 12)

print(amy.greets())
print(archie.greets())
print(archie.check_if_slow_or_fast())
print(amy.check_if_slow_or_fast())

if amy.is_nickname_long():
    print(amy.greets())

if archie.is_nickname_long():
    print(archie.greets())


class Car:
    number_of_wheels = 4
    made_of_steel = True

    def __init__(self, owner_name, brand, color, type_of_fuel, is_working): #constructor
        self.owner_name = owner_name
        self.brand = brand
        self.color = color
        self.type_of_fuel = type_of_fuel
        self.is_working = is_working

    def start_the_car(self):
        if self.is_working:
            return f"{self.owner_name}'s car goes... Vroom vroom"
        else:
            return f"{self.owner_name}'s car goes... enhhhhhh"

    def is_fancy(self):
        fancy_cars = ["bmw", "audi", "jeep"]
        
        if self.brand in fancy_cars:
            return f"{self.owner_name}'s car is a fancy car"
        else:
            return f"{self.owner_name}'s car is not a fancy car"
        
buntys_car = Car("bunty", "suzuki", "white", "petrol", True)

shantys_car = Car("shanty", "bmw", "grey", "diesel", False)

result1 = buntys_car.start_the_car()
result2 = shantys_car.start_the_car()
buntys_car.number_of_wheels


# copying the class body, (Inheritence)
class CheapCars(Car):
    is_cheap = True
    is_affordable = True

    def start_the_car(self):
        if self.is_working:
            return f"{self.owner_name}'s car goes... Vroom vroom but slowww"
        else:
            return f"{self.owner_name}'s car goes... enhhhhhh"


random_car = CheapCars("tany", "audi", "grey", "diesel", True)
print(random_car.start_the_car())