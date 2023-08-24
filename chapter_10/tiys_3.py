import json;
"""
10-11. Favorite Number: Write a program that prompts for the user’s favorite number. Use
json.dump() to store this number in a file. Write a separate program that reads in this value
and prints the message, “I know your favorite number! It’s _____.”
10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11
into one file. If the number is already stored, report the favorite number to the user. If not,
prompt for the user’s favorite number and store it in a file. Run the program twice to see that it
works.
"""

def get_fav_num(filename):
    fav_num = input("What is your favorite number: ");
    with open(filename, 'w') as file_obj:
        json.dump(int(fav_num), file_obj);
        print(f"Got it, your favourite number is: {fav_num}");

def fav_number(filename):
    try:
        with open(filename) as file_obj:
            fav_num = json.load(file_obj);
    except json.JSONDecodeError:
        get_fav_num(filename);
    except FileNotFoundError:
        get_fav_num(filename);
    else:
        print(f"Your favourite number is: {fav_num}");

#get_fav_num("chapter_10/text_files/tiys_json.json");
#fav_number("chapter_10/text_files/tiys_json.json");

"""
10-13. Verify User: The final listing for remember_me.py assumes either that the user has
already entered their username or that the program is running for the first time. We should
modify it in case the current user is not the person who last used the program.
Before printing a welcome back message in greet_user(), ask the user if this is the correct
username. If it’s not, call get_new_username() to get the correct username.
"""
def what_is_your_name(filename):
    username = input("What is your name? ")
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj);
        print(f"YOU WILL NOT BE FORGOTTEN {username}");

def greet_user(filename):
    get_username = input(f"What is your username? ");
    try:
        with open(filename) as file_obj:
            username = json.load(file_obj);
            if get_username.lower() == username.lower():
                print(f"Welcome back, {username}");
            else:
                print(f"Username: '{get_username}' is not found.\nYou will be prompted to create a username.");
                what_is_your_name(filename);
    except json.JSONDecodeError:
        what_is_your_name(filename);
    except FileNotFoundError:
        what_is_your_name(filename);

greet_user("chapter_10/text_files/numbers.json");