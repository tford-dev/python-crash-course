import json;

def json_dump():
    numbers = [2, 3, 5, 7, 11, 13];
    filename = "chapter_10/text_files/numbers.json";
    with open(filename, 'w') as file_obj:
        json.dump(numbers, file_obj);

#json_dump();

def json_load():
    filename = "chapter_10/text_files/numbers.json";
    with open(filename) as file_obj:
        numbers = json.load(file_obj);
    print(numbers);

#json_load();

def remember_me():
    username = input("What is your name? ");
    filename = "chapter_10/text_files/numbers.json";
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj);
        print(f"YOU WILL NOT BE FORGOTTEN {username}");

#remember_me();
def what_is_your_name(filename):
    username = input("What is your name? ")
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj);
        print(f"YOU WILL NOT BE FORGOTTEN {username}");

def greet_user(filename):
    try:
        with open(filename) as file_obj:
            username = json.load(file_obj);
    except json.JSONDecodeError:
        what_is_your_name(filename);
    except FileNotFoundError:
        what_is_your_name(filename);
    else: 
        print(f"Welcome back, {username}");

greet_user("chapter_10/text_files/numbers.json");