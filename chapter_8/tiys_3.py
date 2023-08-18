"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call
provides, and it should print a summary of the sandwich that’s being ordered. Call the function
three times, using a different number of arguments each time.
"""
def sandwiches(*items_list):
    string_list = [];
    for item in items_list:
        string_list.append(item);
    if (len(items_list) > 2):
        #item_list = items_list;
        last_item = string_list.pop();
        separator = ", " 
        chopped_string = separator.join(string_list);
        complete_string = f"You would like {chopped_string}, and {last_item} on your sandwich.";
    elif (len(items_list) == 2):
        complete_string = f"You would like {string_list[0]} and {string_list[1]} on your sandwich.";
    else:
        complete_string = f"You would like {string_list[0]} on your sandwich."
    print(complete_string);
        

sandwiches("turkey", "lettuce", "tomato", "mayonnaise");
sandwiches("ham", "swiss cheese");
sandwiches("roast beef");

"""
8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a profile of
yourself by calling build_profile(), using your first and last names and three other key-value
pairs that describe you.
"""
def process_terminated():
    print("Proccess terminated.");

def build_profile(**user_info):    
    while True:
        print("Welcome to the build-user-profile terminal.");
        print("Please enter the valid value for each prompt.");
        print("Enter 'q' to terminate session or 'f' to finish entry.");
        def get_name(part_of_name):
            user_info[part_of_name] = input(f"Please enter your {part_of_name}: ")
            while user_info[part_of_name].lower() == 'f':
                user_info[part_of_name] = input(f"Please enter your {part_of_name}: ")
            if (user_info[part_of_name].lower() == 'q'):
                process_terminated();
                return False;
            return True;
    
        if not get_name('first name'):
            break;
        if not get_name('last name'):
            break;
    
        while True:
            make_key = input("Enter a key for a key-value pair that you would like to add to your user profile: ")
            if make_key.lower() == 'q':
                user_info = {};
                process_terminated();
                return False;
            while make_key.lower() != 'f':
                user_info[make_key] = input("Please enter a value for the key you just entered: ");
                break;
            if make_key.lower() == 'f':
                print(user_info);
                return False;

#build_profile();

"""
8-14. Cars: Write a function that stores information about a car in a dictionary. The function
should always receive a manufacturer and a model name. It should then accept an arbitrary
number of keyword arguments. Call the function with the required information and two other
name-value pairs, such as a color or an optional feature.
"""

def make_car(make, model, **optional_feature):
    car_dict = {};
    car_dict['make'] = make;
    car_dict['model'] = model;
    for key, value in optional_feature.items():
        car_dict[key] = value;
    print(car_dict);

#make_car('toyota', 'camry', color='green', tow_package=True);