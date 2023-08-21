class Dog:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def sit(self):
        print(f"{self.name} is now sitting.");

    def roll_over(self):
        print(f"{self.name} rolled over!");

my_dog = Dog('Willie', 6);

""" print(my_dog.name, my_dog.age);
my_dog.sit();
my_dog.roll_over(); """

class Car: 
    def __init__(self, make, model, year):
        self.make = make;
        self.model = model;
        self.year = year;
        self.odometer_reading = 0;

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}";
        return long_name.title();

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it");

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage;
        else:
            print("You can't roll back an odometer!");

    def increment_odometer(self, miles):
        self.odometer_reading += miles;

""" test_car = Car(make="toyota", model="camry", year=2020);
print(test_car.get_descriptive_name()); """
class Battery: 
    def __init__(self, battery_size=75):
        self.battery_size = battery_size;

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.");

    def get_range(self):
        if self.battery_size == 75:
            range = 260;
        elif self.battery_size == 100:
            range = 315;
        print(f"This car can go for damn near {range} miles on a full charge, I reckon.");

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year);
        self.battery_size = 75;
        self.battery = Battery();

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery");

my_tesla = ElectricCar(make="tesla", model="model s", year=2019);
print(my_tesla.get_descriptive_name());
my_tesla.battery.describe_battery();
my_tesla.battery.get_range();

#-------import templates------------------------------------------------------------
#from car import ElectricCar
#from car import Car, ElectricCar -this is to import multiple classes
#import car -this is to import an entire module
#from module_name import *
#from car import car -importing a Module into a Module
#from electric_car import ElectricCar as EC -Using Aliases
