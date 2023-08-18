"""
5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.
Imagine you are writing code that will print a greeting to each user after they log in to a
website. Loop through the list, and print a greeting to each user:
If the username is 'admin', print a special greeting, such as Hello
admin, would you like to see a status report?
Otherwise, print a generic greeting, such as Hello Jaden, thank you
for logging in again.
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
If the list is empty, print the message We need to find some users!
Remove all of the usernames from your list, and make sure the
correct message is printed.
"""
USERNAME_LIST = ["conj", "admin", "dairystatus", "mutalize", "fordbear"];
EMPTY_TEST_ARRAY = [];

def hello_admin(list_arr):
    if len(list_arr) > 0:
        for user in list_arr:
            if user == "admin":
                print(f"Greetings, dear {user}. \nOur overlord, {user}.");
            else:
                print(f"Welcome back {user}!");
    else: 
        print("The list is empty, bro.");

hello_admin(USERNAME_LIST);
hello_admin(EMPTY_TEST_ARRAY);

"""
5-10. 
Checking Usernames: Do the following to create a program that simulates how
websites ensure that everyone has a unique username.
Make a list of five or more usernames called current_users.
Make another list of five usernames called new_users. Make sure one
or two of the new usernames are also in the current_users list.
Loop through the new_users list to see if each new username has
already been used. If it has, print a message that the person will
need to enter a new username. If a username has not been used,
print a message saying that the username is available.
Make sure your comparison is case insensitive. If 'John' has been
used, 'JOHN' should not be accepted. (To do this, you’ll need to
make a copy of current_users containing the lowercase versions of all
existing users.)
"""

CURRENT_USERS = [
    "CoolCat42",
    "SunnyDays99",
    "TechGuru23",
    "RainbowNinja",
    "StarStrider",
    "PixelMaster",
    "JazzPianoMan",
    "MountainHiker",
    "GamerGeek87"
]

NEW_USERS = [
    "CodeNinja123",
    "SnowflakeGirl",
    "ElectricDreamer",
    "MountainHiker",
    "GamerGeek87"
]

def checking_usernames(list_arr, list_arr_new):
    for current_user in list_arr:
        for new_user in list_arr_new:
            if current_user.lower() == new_user.lower():
                print(f"'{new_user}' is taken. \nPlease pick a unique username.");
                list_arr_new.remove(new_user);
    for new_user in list_arr_new:
        print(f"'{new_user}' has been created");

checking_usernames(CURRENT_USERS, NEW_USERS);

"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd.
Most ordinal numbers end in th, except 1, 2, and 3.
Store the numbers 1 through 9 in a list.
Loop through the list.
Use an if-elif-else chain inside the loop to print the proper ordinal
ending for each number. Your output should read "1st 2nd 3rd 4th
5th 6th 7th 8th 9th", and each result should be on a separate line.
"""
nine_list = [1, 2, 3, 4, 5, 6, 7, 8, 9];

def ordinal_numbers(list_arr):
    for num in list_arr:
        if num > 3:
            print(f"{num}th");
        elif num == 3:
            print(f"{num}rd");
        elif num == 2:
            print(f"{num}nd");
        else:
            print(f"{num}st");

ordinal_numbers(nine_list);