"""
3-10. Every Function: Think of something you could store in a list. For example, you could
make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a
program that creates a list containing these items and then uses each function introduced in this
chapter at least once.
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
#list_arr[:]
def empty_list (list_arr):
    print(f"The length of the list is now {len(list_arr)}");
    print(list_arr);
    print("Now APPENDING a new car at the end of the array called 'tesla roadster'");
    list_arr.append('tesla roadster');
    print(list_arr);
    print("inserting 'toyota camry trd' after the first entry in the array")
    list_arr.insert(1, "toyota camry trd");
    print(list_arr);
    print("removing last item in list/array");
    list_arr.pop();
    print(list_arr);
    print("sorting alphabetically not permanently");
    sorted(list_arr);
    print(list_arr);
    print("sorting in reverse non alphabetized and not permanent");
    sorted(list_arr, reverse=True);
    print(list_arr);
    print("sorting list back in normal order using reverse method...permantly?");
    list_arr.reverse();
    print(list_arr);
    print("now sorting in reverse permanently");
    list_arr.reverse();
    print(list_arr);
    print("Sorts list alphabetically permanently");
    list_arr.sort();
    print(list_arr);
    print(f"Length of list is {len(list_arr)}.");
    print("Clears entired list");
    del list_arr[:];
    print(list_arr);

empty_list(cool_cars);