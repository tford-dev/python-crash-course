"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings
until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add
that topping to their pizza.
"""

def pizza_toppings():
    pizza_list = [];
    prompt = "Tell me your favorite pizza toppings. \nEnter 'quit' to end the program: ";
    message = "";
    while message.lower() != 'quit':
        message = input(prompt);
        if message != 'quit':
            pizza_list.append(message);
            for topping in pizza_list:
                print(f"You chose {topping} as a topping.");
        else: 
            for topping in pizza_list:
                print(f"You chose {topping} as a topping.")
            break;

#pizza_toppings();

"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s
age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is
$10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age,
and then tell them the cost of their movie ticket.
"""
def movie_tickets():
    while True:
        prompt = input("Welcome to this movie theatre.\nHow many years do you have?: ");
        age = int(prompt);
        try:
            if (age < 3):
                print(f"Your age is {age}, so they get in for free!");
            elif (age <= 12 and age >= 3):
                print(f"Your age is {age}, so your ticket is $10!");
            else:
                print(f"Your age is {age}, so your ticket is $15!");
            continue_prompt = input("Press y to continue, press any other key to quit.");
            if(continue_prompt.lower() == 'y'):
                continue;
            else:
                break;
        except ValueError:
            print(f"'{prompt}' is not a valid ")

#movie_tickets();

"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each
of the following at least once:
Use a conditional test in the while statement to stop the loop.
Use an active variable to control how long the loop runs.
Use a break statement to exit the loop when the user enters a 'quit'
value.
"""