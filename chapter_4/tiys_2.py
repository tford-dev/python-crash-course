"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end
of the program that do the following:
Print the message The first three items in the list are:. Then use a
slice to print the first three items from that program’s list.
Print the message Three items from the middle of the list are:. Use a
slice to print three items from the middle of the list.
Print the message The last three items in the list are:. Use a slice to
print the last three items in the list.
"""

cool_cars = [
"subaru wrx sti",
"honda civic type r",
"mitsubishi lancer evolution (evo)",
"nissan skyline gt-r",
"toyota supra",
"mazda rx-7",
"ford mustang gt",
"volkswagen golf gti"
];

def slices(list_arr):
    print(f"The first three items in the list are:");
    for value in list_arr[:3]:
        print(f"{value.title()}");

slices(cool_cars);

"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a
copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
Add a new pizza to the original list.
Add a different pizza to the list friend_pizzas.
Prove that you have two separate lists. Print the message My
favorite pizzas are:, and then use a for loop to print the first list.
Print the message My friend’s favorite pizzas are:, and then use a for
loop to print the second list. Make sure each new pizza is stored in
the appropriate list.
"""
cool_cars_copy = [];

def list_copy(list_arr, list_arr_copy, add_item0, add_item1):
    list_arr_copy = list_arr[:];
    list_arr.append(add_item0);
    list_arr_copy.append(add_item1);
    print("The items of the initial list/array are:")
    for value in list_arr:
        print(f"{value}");
    print("The items of the copied list/array are")
    for value in list_arr_copy:
        print(f"{value}");

list_copy(cool_cars, cool_cars_copy, "inital list*****", "copied list*****");