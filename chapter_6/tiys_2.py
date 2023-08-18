"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new
dictionaries representing different people, and store all three dictionaries in a list called people.
Loop through your list of people. As you loop through the list, print everything you know
about each person.
"""

coach_greg = {
'first_name' : 'greg',
'last_name' : 'adams',
'age' : 48,
'city' : 'las vegas',
},

user_jane = {
'first_name': 'Jane',
'last_name': 'Doe',
'age': 30,
'city': 'New York',
},

engineer_michael = {
'first_name': 'Michael',
'last_name': 'Smith',
'age': 35,
'city': 'San Francisco',
},

people = [coach_greg, user_jane, engineer_michael];

def people_loop(list_arr):
    for person in list_arr:
        for key in person:
            print(f"The user's name is {key['first_name'].title()} {key['last_name'].title()}, they are {key['age']} years old, and are located in {key['city'].title()}!");

people_loop(people);

""" 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each
dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list
called pets. Next, loop through your list and as you do, print everything you know about each
pet """

pets = [
    {
        "pet_name": "fluffy",
        "owner_name": "alice",
        "species": "grizzley bear"
    },
    {
        "pet_name": "bubba",
        "owner_name": "bob",
        "species": "brown bear"
    },
    {
        "pet_name": "blanco",
        "owner_name": "carol",
        "species": "polar bear"
    }
];

def pets_func(list_arr): 
    for pet in list_arr:
        print(f"The pet's name is {pet['pet_name'].title()}, their owner's name is {pet['owner_name'].title()}, and {pet['pet_name'].title()} is a whole {pet['species']}");

pets_func(pets);

"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use
as keys in the dictionary, and store one to three favorite places for each person. To make this
exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop
through the dictionary, and print each person’s name and their favorite places.
"""

favorite_places = {
    "alice": ["beach", "mountains", "Paris"],
    "bob": ["coffee shop", "library", "park"],
    "carol": ["art museum", "countryside", "London"]
}

def the_func(str):
    if " " in str:
        return f"the {str}";
    else: 
        return str;

def places_func(dict_list):
    for person, value in dict_list.items():
        print(f"{person.title()}'s favorite places to visit are {the_func(value[0])}, {the_func(value[1])}, and {the_func(value[2])}");

places_func(favorite_places);

"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each person
can have more than one favorite number. Then print each person’s name along with their
favorite numbers
"""

lucky_num = {
    'kim' : [6, 12,18],
    'Ye' : [7, 14, 21],
    'travis' : [8, 16, 24],
    'kylie' : [9, 18, 27],
    'mike' : [10, 20, 30],
};

def fav_num(dict):
    for key, value in dict.items():
        print(f"The favorite number of {key.title()} is {value[0]}, {value[1]}, and {value[2]}.");

fav_num(lucky_num);

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your
dictionary. Create a dictionary of information about each city and include the country that the
city is in, its approximate population, and one fact about that city. The keys for each city’s
dictionary should be something like country, population, and fact. Print the name of each
city and all of the information you have stored about it.
"""

cities = {
    "new york": {
        "country": "United States",
        "population": 8336817,
        "fact": "New York City is known as the 'Big Apple.'"
    },
    "london": {
        "country": "United Kingdom",
        "population": 8982000,
        "fact": "The London Eye is a popular giant Ferris wheel on the South Bank of the River Thames."
    },
    "tokyo": {
        "country": "Japan",
        "population": 13929286,
        "fact": "Tokyo is home to the world's busiest pedestrian crossing at Shibuya Crossing."
    }
};

def city_func(dict_data):
    for key, value in dict_data.items():
        print(f"The city, {key.title()}, is in the country of {value['country'].title()}, and has a population of {value['population']} people. {value['fact']}");
        

city_func(cities);