"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called
alien_color and assign it a value of 'green', 'yellow', or 'red'.
    Write an if statement to test whether the alien’s color is green. If
    it is, print a message that the player just earned 5 points.
    Write one version of this program that passes the if test and
    another that fails. (The version that fails will have no output.)
"""

""" def alien_colors():
    ALIEN_COLOR = 'green';
    points = 0;
    if (ALIEN_COLOR == 'green'):
        points += 5;
        print(f"Hell yeah, you get 5 points! \nYou now have {points} points.");
    else:
        points -= 5;
        print(f"He's dead but not that color. \nYou now have {points} points.");

alien_colors(); """

"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
If the alien is green, print a message that the player earned 5
points.
If the alien is yellow, print a message that the player earned 10
points.
If the alien is red, print a message that the player earned 15 points.
Write three versions of this program, making sure each message is
printed for the appropriate color alien.
"""
def alien_colors():
    ALIEN_COLOR = 'yellow';
    points = 0;
    if (ALIEN_COLOR == 'green'):
        points += 5;
        print(f"Bro is green, you get 5 points! \nYou now have {points} points.");
    elif (ALIEN_COLOR == 'yellow'):
        points += 10;
        print(f"Bro is yellow, you get 10 points! \nYou now have {points} points.");
    else:
        points += 15;
        print(f"He's dead and red,  you get 15 points. \nYou now have {points} points.");

alien_colors();

"""
5-6. 
Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a
value for the variable age, and then:
If the person is less than 2 years old, print a message that the
person is a baby.
If the person is at least 2 years old but less than 4, print a message
that the person is a toddler.
If the person is at least 4 years old but less than 13, print a message
that the person is a kid.
If the person is at least 13 years old but less than 20, print a
message that the person is a teenager.
If the person is at least 20 years old but less than 65, print a
message that the person is an adult.
If the person is age 65 or older, print a message that the person is
an elder.
"""

def stages_of_life(age):
    if (age < 2):
        print(f"A person who is {age} years old is a baby");
    elif (age > 2 and age < 4):
        print(f"A person who is {age} years old is a toddler");
    elif (age >= 4 and age < 14):
        print(f"A person who is {age} years old is a kid");
    elif (age >= 13 and age < 20):
        print(f"A person who is {age} years old is a teenager");
    elif (age >= 20 and age < 65):
        print(f"A person who is {age} years old is an adult");
    else:
        print(f"A person who is {age} years old is old af");

stages_of_life(1);
stages_of_life(4);
stages_of_life(14);
stages_of_life(20);
stages_of_life(66);

"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent
if statements that check for certain fruits in your list.
Make a list of your three favorite fruits and call it favorite_fruits.
Write five if statements. Each should check whether a certain kind
of fruit is in your list. If the fruit is in your list, the if block should
print a statement, such as You really like bananas! 
"""
FAVORITE_FRUITS = ["grapefruit", "grannysmith apple", "oranges", "pineapples", "watermelon"];

def fruit_function(list_arr):
    for fruit in list_arr:
        if (fruit == "grapefruit" in list_arr):
            print("Grapefruit is tight!");
        elif(fruit == "grannysmith apple" in list_arr):
            print("Apples are tight!");
        elif(fruit == "oranges" in list_arr):
            print("Oranges are tight!");
        elif(fruit == "pineapples" in list_arr):
            print("Pineapples are tight!");              
        else: 
            print("Man what is that?");

fruit_function(FAVORITE_FRUITS);

