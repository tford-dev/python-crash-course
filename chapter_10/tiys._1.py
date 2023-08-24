import datetime
""" 10-3. Guest: Write a program that prompts the user for their name. When they respond, write
their name to a file called guest.txt. """
def guest():
    guest_name = input("Howdy, what is your name? : ");
    file_name = "chapter_10/text_files/guest.txt";
    with open(file_name, 'a') as file_object:
        file_object.write(f"{guest_name.title()}\n");
        print(f"writing to {file_name}: {guest_name.title()}");

#guest();

"""10-4. Guest Book: Write a while loop that prompts users for their name. When they enter
their name, print a greeting to the screen and add a line recording their visit in a file called
guest_book.txt. Make sure each entry appears on a new line in the file."""
def guest_book():
    while True:
        file_name = "chapter_10/text_files/guest_book.txt";
        name_of_user = input("Welcome to Guest Book Terminal.\nEnter 'q' at anytime to quit.\nHowdy, what is your name?");
        if (name_of_user.lower() != "q"):
            with open(file_name, 'a') as file_object:
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p");
                file_object.write(f"{name_of_user.title()}: Checked in at {current_time}\n");
        else:
            print("Terminating process...........................................");
            break;

#guest_book();

"""
10-5. Programming Poll: Write a while loop that asks people why they like programming.
Each time someone enters a reason, add their reason to a file that stores all the responses.
"""
def programming_poll():
    while True:
        file_name = "chapter_10/text_files/programming_poll.txt";
        fav_lang = input("Welcome to the Programming Poll Terminal.\nEnter 'q' at anytime to quit.\nWhy is your favorite programming language your favorite?");
        if (fav_lang.lower() != "q"):
            with open(file_name, 'a') as file_object:
                file_object.write(f"{fav_lang}\n");
                print(f"Your reason: {fav_lang}")
        else:
            print("Terminating process...........................................");
            break;

#programming_poll();
