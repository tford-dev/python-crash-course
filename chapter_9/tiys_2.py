""" 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called
IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or
Exercise 9-4 (page 167). Either version of the class will work; just pick the one you like better.
Add an attribute called flavors that stores a list of ice cream flavors. Write a method that
displays these flavors. Create an instance of IceCreamStand, and call this method. """
from tiys_1 import *
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type);
        self.flavors = [
            "vanilla",
            "chocolate",
            "strawberry",
            "mint chocolate chip",
            "cookies and cream",
            "rocky road",
            "butter pecan",
            "coffee",
            "caramel swirl",
            "pistachio"
        ];
    def flavors_call(self):
        for flavor in self.flavors:
            print(f"An ice cream flavor that is served here is {flavor}");

""" ice_cream = IceCreamStand(restaurant_name="Baskin Robins", cuisine_type="Ice cream");
ice_cream.flavors_call(); """

""" 9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits
from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an
attribute, privileges, that stores a list of strings like "can add post", "can delete post",
"can ban user", and so on. Write a method called show_privileges() that lists the
administrator’s set of privileges. Create an instance of Admin, and call your method. """
class Admin(User):
    def __init__(self, first_name, last_name, location=None, bio=None):
        super().__init__(first_name, last_name, location, bio);
        self.privileges = Privileges();

""" admin = Admin("terry", "stylez", location="richmond, va", bio="test");
admin.show_privileges();
admin.describe_user(); """

""" 9-8. Privileges: Write a separate Privileges class. The class should have one attribute,
privileges, that stores a list of strings as described in Exercise 9-7. Move the
show_privileges() method to this class. Make a Privileges instance as an attribute in the
Admin class. Create a new instance of Admin and use your method to show its privileges. """
class Privileges:
    def __init__(self):
        self.admin_privileges = [
            "User account management",
            "System and network configuration",
            "Software installation and updates",
            "Security policy enforcement",
            "Troubleshooting and technical support",
            "Data backup and recovery",
            "Server management",
            "Network monitoring",
            "Access control management",
            "Infrastructure maintenance",
            "Software license management",
            "Implementing security measures",
            "Network and system optimization",
            "Implementing data privacy policies",
            "Incident response coordination"
        ];
    def show_privileges(self):
        for privilege in self.admin_privileges:
            print(privilege);

""" admin = Admin("terry", "stylez", location="richmond, va", bio="test");
admin.privileges.show_privileges();
admin.describe_user(); """

""" 9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method
to the Battery class called upgrade_battery(). This method should check the battery size and
set the capacity to 100 if it isn’t already. Make an electric car with a default battery size, call
get_range() once, and then call get_range() a second time after upgrading the battery. You
should see an increase in the car’s range. """

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

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100;

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
my_tesla.battery.upgrade_battery();
my_tesla.battery.get_range();