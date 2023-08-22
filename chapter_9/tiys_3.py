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
matching these four numbers or letters wins a prize. """

class Lottery:
    def __init__(self, lottery_data=[]):
        self.lottery_data = lottery_data;

    def choose_num(self):
        lot_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 'a', 'b', 'c', 'd', 'e'];
        for i in range(5):
            random_int = random.randint(1, len(lot_num) - 1);
            select_num = lot_num[random_int];
            self.lottery_data.append(select_num);

    def show_num(self):
        self.choose_num();
        separator = ", ";
        num_string = separator.join(map(str, self.lottery_data));
        print(f"The lottery numbers are: {num_string}");

winning_num = Lottery();
winning_num.show_num();