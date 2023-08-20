"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant
should store two attributes: a restaurant_name and a cuisine_type. Make a method called
describe_restaurant() that prints these two pieces of information, and a method called
open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually,
and then call both methods.
"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name;
        self.cuisine_type = cuisine_type;

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is lit!");
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type}.");

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.");

restaurant = Restaurant("Wendy's", "burgers and fries");
#restaurant.describe_restaurant();
#restaurant.open_restaurant();

"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different
instances from the class, and call describe_restaurant() for each instance.
"""
restaurant_0 = Restaurant("Spice Delight", "Indian")
#restaurant_0.describe_restaurant();
restaurant_1 = Restaurant("La Trattoria Bella", "Italian")
#restaurant_1.describe_restaurant();
restaurant_2 = Restaurant("Sushi Palace", "Japanese")
#restaurant_2.describe_restaurant();

"""
9-3. Users: Make a class called User. Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile. Make a
method called describe_user() that prints a summary of the user’s information. Make another
method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
"""
class User:
    def __init__(self, first_name, last_name, location=None, bio=None):
        self.first_name = first_name;
        self.last_name = last_name;
        self.location = location;
        self.bio = bio;

    def describe_user(self):
        if(self.location and self.bio):
            print(f"{self.first_name.title()} {self.last_name.title()} is from {self.location.title()}.");
            print(self.bio)
        elif(self.location and self.bio == None):
            print(f"{self.first_name.title()} {self.last_name.title()} is from {self.location.title()}.")
        elif(self.bio and self.location == None):
            print(f"The user {self.first_name.title()} {self.last_name.title()} has their bio as {self.bio}.")
        else:
            print(f"{self.first_name.title()} {self.last_name.title()}");

test0 = User("terry", "stylez", "richmond, va", "The most prolific mediocre DJ in all of Virginia.");
test0.describe_user();

test1 = User("terry", "stylez", location="richmond, va");
test1.describe_user()

test2 = User("terry", "stylez", bio="The most prolific mediocre DJ in all of Virginia");
test2.describe_user()

test3 = User("terry", "stylez");
test3.describe_user()