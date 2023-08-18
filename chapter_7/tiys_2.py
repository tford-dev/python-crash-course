"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches. Loop through the list of sandwich
orders and print a message for each order, such as I made your tuna sandwich. As each
sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been
made, print a message listing each sandwich that was made.
"""
def deli():
    sandwiches = [
    "ham and cheese",
    "turkey club",
    "blt",
    "grilled cheese",
    "roast beef"
    ];
    finished_sandwiches = [];
    while sandwiches:
        sandwich = sandwiches.pop();
        print(f"Your order for a {sandwich.title()} sandwich is in progress.");
        finished_sandwiches.append(sandwich);
        print(f"Your {sandwich.title()} sandwich has been prepared and is ready for pickup.");
    for finished_sandwich in finished_sandwiches:
        print(f"{finished_sandwich.title()} is complete.");

#deli();

""" 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich
'pastrami' appears in the list at least three times. Add code near the beginning of your
program to print a message saying the deli has run out of pastrami, and then use a while loop
to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami
sandwiches end up in finished_sandwiches. 
"""
def no_pastrami():
    sandwiches = [
    "ham and cheese",
    "pastrami and cheese",
    "turkey club",
    "pastrami and cheese",
    "blt",
    "grilled cheese",
    "roast beef",
    "pastrami and cheese",
    ];
    finished_sandwiches = [];
    while "pastrami and cheese" in sandwiches:
        sandwiches.remove("pastrami and cheese");
        print("Ha ha ha, there is no pastrami. ha ha ha");
    while sandwiches:
        sandwich = sandwiches.pop();
        print(f"Your order for a {sandwich.title()} sandwich is in progress.");
        finished_sandwiches.append(sandwich);
        print(f"Your {sandwich.title()} sandwich has been prepared and is ready for pickup.");
    for finished_sandwich in finished_sandwiches:
        print(f"{finished_sandwich.title()} is complete.");
    print(finished_sandwiches);

#no_pastrami();

"""
7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a
prompt similar to If you could visit one place in the world, where would you go? Include a block of
code that prints the results of the poll.
"""

def dream_vacation():
    responses = {};
    active_poll = True;
    while active_poll:
        name = input("Howdy, what is your name?: ");
        response = input("What is the location of your dream vacation???: ")
        #Take note, this is how you create a key and assign a value to an empty dictionary
        responses[name] = response;
        repeat = input("Would you like have someone else respond? (y/n): ");
        if((repeat.lower() == 'y') or (repeat.lower() == 'yes')):
            continue;
        else:
            active_poll = False;
    print("Printing dictionary of poll... Please Standy By...");
    for name, response in responses.items():
        print(f"{name.title()} would like to go to {response} for their dream vacation.");

dream_vacation();