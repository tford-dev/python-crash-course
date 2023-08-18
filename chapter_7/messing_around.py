def test_func0():
    message = input("Give me some input bro: ");
    print(message);

#test_func0();

def test_func1():
    name = input("Give me your name: ");
    print(f"What's good, {name.title()}?");

#test_func1();

def test_func2():
    prompt = "I'm going to add more to this prompt in the next line.";
    prompt += "\n This is a new line, enter your name or be executed: ";
    name = input(prompt);
    print(f"\nHey, {name.title()}! You are spared.");

#test_func2();

def test_func3():
    age = input("How many years do you have?: ");
    print(f"You have {int(age)} years.");

#test_func3();

def test_func4():
    age = input("How many years do you have?: ");
    age = int(age);
    if(age < 21):
        print(f"You are {age} years old so no Hornitos for you!!!")
    else:
        print(f"You are {age} years old so grab some limes!");

#test_func4();

def confirmed():
    unconfirmed_users = ["kylie", "travis", "kanye", "kim"];
    confirmed_users = [];
    while unconfirmed_users:
        current_user = unconfirmed_users.pop();
        print(f"Verifying user: {current_user.title()}");
        confirmed_users.append(current_user);
    print("\nThe following users have been confirmed: ");
    for confirmed_user in confirmed_users:
        print(confirmed_user.title());

#confirmed();

#clear item in list
def test_func6():
    hollywood = ["kylie", "travis", "kanye", "kim", "travis", "travis"];
    while 'travis' in hollywood:
        hollywood.remove('travis');
        print("Removing user in hollywood");
    print(hollywood);

#test_func6();

def test_func7():
    #empty dictionary
    responses = {}
    #active flag
    polling_active = True;
    #true above ^
    while polling_active:
        name = input("WHAT IS YOUR NAME????")
        response = input("Who do you want to eat dinner with who is alive today?: ");
        #Take note, this is how you create a key and assign a value to an empty list
        responses[name] = response;
        #polling_active is true so someone responds with no, the loop restarts.
        repeat = input("Would you like have someone else respond? (y/n): ");
        if((repeat.lower() == 'y') or (repeat.lower() == 'yes')):
            continue;
        else:
            polling_active = False;
    print("------Poll Results------");
    for name, response in responses.items():
        print(f"{name} would like to have dinner with {response}");

test_func7();
