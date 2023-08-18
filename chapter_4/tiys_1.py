#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
def count_to_twenty():
    print("Use a for loop to print the numbers from 1 to 20, inclusive.");
    for num in range(1,21):
        print(num);

count_to_twenty();

"""
4-5. Summing a Million: Make a list of the numbers from one to one million, and then use
min() and max() to make sure your list actually starts at one and ends at one million. Also, use
the sum() function to see how quickly Python can add a million numbers.
"""
def summing_a_million():
    print("Printing max and min in 1,000,000.");
    million_list = list(range(1,1000001));
    print(f"The minimum of a million is {min(million_list)}.");
    print(f"The maximum of a million is {max(million_list)}.");

summing_a_million();

"""
4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd
numbers from 1 to 20. Use a for loop to print each number.
"""

def print_odd():
    print("Printing odd numbers from 1-20.");
    odds_in_twenty = [];
    for num in range(1,21,2):
        odds_in_twenty.append(num);
    print(odds_in_twenty);

print_odd();

"""
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the
numbers in your list.
"""
def threes_func():
    print("Make a list of the multiples of 3 from 3 to 30");
    mults_of_three = [];
    for num in range(0,31,3):
        if num > 0:
            mults_of_three.append(num);
            print(f"{num} divided by 3 is {int(num / 3)}.");

threes_func();

"""
4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is
written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer
from 1 through 10), and use a for loop to print out the value of each cube.
"""

def cubed():
    print("Cubing numbers 1-10");
    ten_list = list(range(1,11));
    cubed_list = [];
    for num in ten_list:
        cubed_list.append(num**3);
    print(cubed_list);

cubed();

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
def cubed_comprehension():
    print("Cubing numbers 1-10 with a comprehension list");
    cubes = [num**3 for num in range(1,11)];
    print(cubes);

cubed_comprehension();