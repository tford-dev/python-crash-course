"""
6-1. Person: Use a dictionary to store information about a person you know. Store their first
name, last name, age, and the city in which they live. You should have keys such as first_name,
last_name, age, and city. Print each piece of information stored in your dictionary
"""

coach_greg = {
    'first_name' : 'greg',
    'last_name' : 'adams',
    'age' : 48,
    'city' : 'las vegas',
};

def print_dict(dict):
    print(f"{dict['first_name'].title()}, \n{dict['last_name'].title()}, \n{dict['age']}, \n{dict['city'].title()}");

print_dict(coach_greg);

"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five
names, and use them as keys in your dictionary. Think of a favorite number for each person,
and store each as a value in your dictionary. Print each person’s name and their favorite
number. For even more fun, poll a few friends and get some actual data for your program.
"""
lucky_num = {
    'kim' : 6,
    'Ye' : 7,
    'travis' : 8,
    'kylie' : 9,
    'mike' : 10
}

def fav_num(dict):
    for key in dict:
        print(f"The favorite number of {key.title()} is {dict[key]}.");

fav_num(lucky_num);

"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to
avoid confusion, let’s call it a glossary.
Think of five programming words you’ve learned about in the
previous chapters. Use these words as the keys in your glossary,
and store their meanings as values.
Print each word and its meaning as neatly formatted output. You
might print the word followed by a colon and then its meaning, or
print the word on one line and then print its meaning indented on
a second line. Use the newline character (\n) to insert a blank line
between each word-meaning pair in your output.
"""
glossary_dict = {
    'dns' : 'domain name service',
    'ospf' : 'open shortest path first',
    'vlan' : 'virtual local area network',
    'eigrp' : 'enhanced interior gateway routing protocol',
    'mpls' : 'multi protocol label service',
};

def glossary(dict):
    for key in dict:
        print(f"{key.upper()} stands for {dict[key]}.")

glossary(glossary_dict);