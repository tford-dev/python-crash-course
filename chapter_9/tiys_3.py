import random;
"""
9-13. 
Dice: Make a class Die with one attribute called sides, which has a default value of 6.
Write a method called roll_die() that prints a random number between 1 and the number of
sides the die has. 
Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        for i in range(11):
            random_int = random.randint(1, self.sides);
            print(random_int);


new_die = Dice(6);
ten_die = Dice(10);
twenty_die = Dice(20);
#ten_die.roll_die();

""" 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five letters.
Randomly select four numbers or letters from the list and print a message saying that any ticket
matching these four numbers or letters wins a prize.

9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of
lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling
numbers until your ticket wins. Print a message reporting how many times the loop had to run
to give you a winning ticket.
"""

""" class Lottery:
    def __init__(self):
        self.lottery_data = [];
        self.ticket_list = [];
        self.lottery_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 'a', 'b', 'c', 'd', 'e'];
        self.lottery_num_string = None;
        self.player_num_string = None;
        self.num_of_tries = 0;
        
    def choose_num(self):
        self.lottery_data = [];
        for i in range(5):
            random_int = random.randint(0, len(self.lottery_numbers) - 1);
            select_num = self.lottery_numbers[random_int];
            self.lottery_data.append(select_num);

    def show_num(self):
        separator = ", ";
        self.lottery_num_string = separator.join(map(str, self.lottery_data));
        print(f"The lottery numbers are: {self.lottery_num_string}");

    def my_ticket(self):
        self.ticket_list = [];
        self.player_num_string = None;
        for i in range(5):
            random_int = random.randint(0, len(self.lottery_numbers) - 1);
            select_num = self.lottery_numbers[random_int];
            self.ticket_list.append(select_num);
        separator = ", ";
        self.player_num_string = separator.join(map(str, self.ticket_list));
        print(f"ticket string : {self.player_num_string}");

    def play(self):
        while True:
            self.choose_num();
            self.show_num();
            self.my_ticket();
            if(self.lottery_num_string == self.player_num_string):
                print(f"The winning numbers {self.lottery_data} match your numbers: {self.player_num_string}.\nIt took you {self.num_of_tries} tries. \nYou're rich for a little while.");
                break;
            else:
                self.num_of_tries += 1;
                print("You lose. Spend $20 more dollars on a ticket.");

winning_num = Lottery();
winning_num.play(); """
# winning_num.choose_num();
# winning_num.show_num();
# winning_num.my_ticket()

class Lottery:
    def __init__(self):
        self.lottery_data = [];
        self.ticket_list = [];
        self.lottery_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 'a', 'b', 'c', 'd', 'e'];
        self.lottery_num_string = "";
        self.player_num_string = "";
        self.num_of_tries = 0;
        
    def choose_num(self, list_arr, destination_str=""):
        list_arr = [];
        for i in range(5):
            random_int = random.randint(0, len(self.lottery_numbers) - 1);
            select_num = self.lottery_numbers[random_int];
            list_arr.append(select_num);
        separator = ", ";
        choose_num_str = separator.join(map(str, list_arr));
        setattr(self, destination_str, choose_num_str);
        print(destination_str);

    def play(self):
        while True:
            self.choose_num(self.lottery_data, "lottery_num_string");
            self.choose_num(self.ticket_list, "player_num_string");
            print(self.lottery_num_string);
            print(self.player_num_string);
            if(self.lottery_num_string == self.player_num_string):
                print(f"The winning numbers {self.lottery_num_string} match your numbers: {self.player_num_string}.\nIt took you {self.num_of_tries} tries. \nYou're rich for a little while.");
                break;
            else:
                self.num_of_tries += 1;
                print(f"The lottery numbers are: {self.lottery_num_string}. \nYour numbers are {self.player_num_string}")
                print("You lose. Spend $20 more dollars on a ticket.");

winning_num = Lottery();
winning_num.play();