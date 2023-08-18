"""
7-1. Rental Car: Write a program that asks the user what kind of rental car they would like.
Print a message about that car, such as “Let me see if I can find you a Subaru.”
"""

def rental_car():
    prompt = input("What make of car would you like???: ");
    print(f"Let me see if I can find you a {prompt.title()}.");

#rental_car();

"""
7-2. Restaurant Seating: Write a program that asks the user how many people are in their
dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a
table. Otherwise, report that their table is ready.
"""

def restaurant_seating():
    num_of_seats = input("How many people will be dining tonight?: ");
    if (int(num_of_seats) > 8):
        print("You will have to wait for seating!");
    else:
        print("Right this way!");

#restaurant_seating();

"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a
multiple of 10 or not.
"""
def multiples_of_ten():
    while True:
        try:
            num_prompt = input("Give me a number that is a multiple of ten: ");
            int_num = int(num_prompt);
            if(int_num):
                if(int_num % 10 == 0):
                    print(f"{int_num} divided by 10 equals {int_num}. So it is indeed a multiple of 10.");
                    continue_prompt = input("Press y to continue, press any other key to quit.");
                    if(continue_prompt.lower() == 'y'):
                        continue;
                    else:
                        break;
                else: 
                    print(f"{int_num} divided by 10 equals {int_num/10}. {int_num} is ***NOT*** a multiple of 10.");
                    continue_prompt = input("Press y to continue, press any other key to quit.");
                    if(continue_prompt.lower() == 'y'):
                        continue;
                    else:
                        break;
        except ValueError: 
            print(f"'{num_prompt}' is not an integer, try again!!!")
            continue_prompt = input("Press y to continue, press any other key to quit.");
            if(continue_prompt.lower() == 'y'):
                continue;
            else:
                break;


multiples_of_ten();