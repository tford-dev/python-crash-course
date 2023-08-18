"""
3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s
name by accessing each element in the list, one at a time.
"""
NAME_LIST = ["darius", "william", "grant", "dominic"];
for name in NAME_LIST:
    print(name.title());

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each
person’s name, print a message to them. The text of each message should be the same, but each
message should be personalized with the person’s name.
"""
def name_strings(name_list):
    for name in name_list:
        if name == "darius":
            print(f"{name.title()} is too childish.");
        elif name == "william":
            print(f"{name.title()} is that chocolate boy.");
        elif name == "grant":
            print(f"{name.title()} has a lot of cars.");
        else:
            print(f"{name.title()} lives in Maryland for some reason.");

name_strings(NAME_LIST);

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a
car, and make a list that stores several examples. Use your list to print a series of statements
about these items, such as “I would like to own a Honda motorcycle.”
"""
COOL_CARS = ["toyota supra", "subaru wrx", "honda type-r", "toyota 86"]

def car_strings(list_arr):
    for car in list_arr:
        print(f"Having a {car.title()} would be lit!");

car_strings(COOL_CARS);