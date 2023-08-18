"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you create to ten.
If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have
at least one True and one False result for each of the following:
Tests for equality and inequality with strings
Tests using the lower() method
Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
Tests using the and keyword and the or keyword
Test whether an item is in a list
Test whether an item is not in a list
"""

cool_cars = [
"subaru wrx sti",
"honda civic type r",
"mitsubishi lancer evolution (evo)",
"nissan skyline gt-r",
"toyota supra",
"mazda rx-7",
"ford mustang gt",
"Volkswagen golf gti"
];

num_list = list(range(1,11));

def conditonal_func(list_arr, num_list_arr):
    print("Tests for equality and inequality with strings");
    print(list_arr[0] == list_arr[1]); #false

    print("Tests using the lower() method");
    print(list_arr[7].lower() == "Volkswagen golf gti"); #false

    print("Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to");
    print(f"10 > 7 is {num_list_arr[9] > 7}") #true
    print(f"10 <= 7 is {num_list_arr[9] <= 7}") #false
    print(f"5 < 4 is {num_list_arr[4] < 4}") #false
    print(f"5 >= 5 is {num_list_arr[4] >= 5}") #true
    print(f"5 != 5 is {num_list_arr[4] != 5}") #false
    print(f"5 == 5 {num_list_arr[4] == 5}") #true

    print("Test whether an item is in a list");
    print(f"'nissan skyline gt-r' is in car array/list:{'nissan skyline gt-r' in list_arr}"); #true

    print("Test whether an item is not in a list");
    print(f"'toyota camry' is in car array/list:{'toyota camry' in list_arr}"); #false

    print("Tests using the and keyword and the or keyword");
    if(list_arr[0] == "subaru wrx sti" and num_list_arr[4] == 5):
        print("The conditional statement is true!");
    else:
        print("False broooooooooo");
    
conditonal_func(cool_cars, num_list);

    