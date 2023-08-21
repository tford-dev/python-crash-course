"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute
called number_served with a default value of 0. Create an instance called restaurant from this
class. Print the number of customers the restaurant has served, and then change this value and
print it again.
Add a method called set_number_served() that lets you set the number of customers that
have been served. Call this method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment the number of
customers who’ve been served. Call this method with any number you like that could represent
how many customers were served in, say, a day of business.
"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name;
        self.cuisine_type = cuisine_type;
        self.number_served = 0;

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is lit!");
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type}.");
        print(f"{self.restaurant_name.title()} has served {self.number_served} customers!");

    def set_number_served(self, num):
        self.number_served = num;
    
    def increment_number_served(self, num):
        self.number_served += num;

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.")

# wendys = Restaurant("Wendy's", "burgers and fries", 0);
# wendys.set_number_served(3000000);
# wendys.increment_number_served(999);
# wendys.describe_restaurant();

"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class from
Exercise 9-3 (page 162). Write a method called increment_login_attempts() that increments
the value of login_attempts by 1. Write another method called reset_login_attempts() that
resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly, and then call
reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
"""

class User:
    def __init__(self, first_name, last_name, location=None, bio=None):
        self.first_name = first_name;
        self.last_name = last_name;
        self.location = location;
        self.bio = bio;
        self.login_attempts = 0;

    def show_attempts(self):
        print(f"{self.first_name.title()} {self.last_name.title()} has {self.login_attempts} login attempts.");

    def increment_login_attempts(self):
        self.login_attempts += 1;
        self.show_attempts();
    
    def reset_login_attempts(self):
        self.login_attempts = 0;
        self.show_attempts()

    def describe_user(self):
        if (self.location and self.bio):
            print(f"{self.first_name.title()} {self.last_name.title()} is from {self.location.title()}.")
            print(self.bio)
        elif (self.location and self.bio == None):
            print(f"{self.first_name.title()} {self.last_name.title()} is from {self.location.title()}.")
        elif (self.bio and self.location == None):
            print(f"The user {self.first_name.title()} {self.last_name.title()} has their bio as {self.bio}.")
        else:
            print(f"{self.first_name.title()} {self.last_name.title()}")


""" test0 = User("terry", "stylez", "richmond, va", "The most prolific mediocre DJ in all of Virginia.");
test0.describe_user();
test0.increment_login_attempts();
test0.increment_login_attempts();
test0.increment_login_attempts() """

"""
test1 = User("terry", "stylez", location="richmond, va")
test1.describe_user()

test2 = User("terry", "stylez", bio="The most prolific mediocre DJ in all of Virginia")
test2.describe_user()

test3 = User("terry", "stylez")
test3.describe_user()
"""