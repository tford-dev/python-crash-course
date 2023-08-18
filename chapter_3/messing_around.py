bicycles_list = ['sunday', 'subrosa', 'stolen', 'cult'];
print(bicycles_list[0].title());
print(f"{bicycles_list[1].title()} \n{bicycles_list[3].title()}");
print(f"{bicycles_list[-1].title()} is the last item in the list/array.");

bicycles_list[1] = 'haro';

bicycles_list.append('fiend');

print(bicycles_list);

CARS_LIST = [
    "Subaru WRX STI",
    "Honda Civic Type R",
    "Mitsubishi Lancer Evolution (Evo)",
    "Nissan Skyline GT-R",
    "Toyota Supra",
    "Mazda RX-7",
    "Ford Mustang GT",
    "Volkswagen Golf GTI"
];

cool_cars = [];

def cool_cars_list(from_list_arr, to_list_arr):
    for car in from_list_arr:
        to_list_arr.append(car);
    print(to_list_arr);

cool_cars_list(CARS_LIST, cool_cars);

cool_cars.insert(0, 'Toyota TRD');
del cool_cars[1];
cool_cars.pop(0);
cool_cars.remove("Mitsubishi Lancer Evolution (Evo)");
cool_cars.sort(); #sorts a list in alphabetical order
cool_cars.sort(reverse=True); #sorts a list in reverse alphabetical order
sorted(cool_cars); #sorts cars alphabetically without actually changing order of list - not permanent
cool_cars.reverse() #reverse the original order of list(not alphabetical)
len(cool_cars) #length of list
print(cool_cars);