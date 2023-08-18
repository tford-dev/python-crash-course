def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}";
    else:
         full_name = f"{first_name} {last_name}";
    
    return full_name.title();

musician = get_formatted_name('kanye', 'west', 'omari')
# print(musician);

def name_of_user():
    while True:
        print("Please, tell me your government name:");
        print("(Enter 'q' at any time to quit, you coward.)");
        first_name = input("First name: ");
        if (first_name.lower() == 'q'):
            print("Process aborted.");
            break;
        last_name = input("Last name: ");
        if (last_name.lower() == 'q'):
            print("Process aborted.");
            break;
        middle_name = input("*Middle name is optional* Enter 's' if you wish to skip. \nMiddle name: ")
        if ((middle_name.lower() == 's') or (middle_name.lower() == '')):
            middle_name = None;
        formatted_name = get_formatted_name(first_name, last_name, middle_name);
        print(f"You have shown bravery, {formatted_name}.");

#name_of_user();

def kanye_tracks(*tracks):
    for track in tracks:
        print(track.title());

kanye_tracks("power");
kanye_tracks("power", "through the wire", "touch the sky");