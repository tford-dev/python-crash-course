"""
6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs
through. One key-value pair might be 'nile': 'egypt'.
Use a loop to print a sentence about each river, such as The Nile
runs through Egypt.
Use a loop to print the name of each river included in the
dictionary.
Use a loop to print the name of each country included in the
dictionary.
"""

exercises = {
    'push' : 'bench press',
    'pull' : 'deadlifts',
    'legs' : 'squats'
}

def exercise_func(dict):
    for key, value in dict.items():
        print(f"For {key} day, spam {value}!");

exercise_func(exercises);

"""
6-6. Polling: Use the code in favorite_languages.py (page 97).
Make a list of people who should take the favorite languages poll.
Include some names that are already in the dictionary and some
that are not.
Loop through the list of people who should take the poll. If they
have already taken the poll, print a message thanking them for
responding. If they have not yet taken the poll, print a message
inviting them to take the poll.
"""

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'jill': '',
'jack': '',
'joel': ''
}

def polling(dict):
    for key, value in dict.items():
        if value == '':
            print(f"{key.title()} is invited to take the languages survey");
        else:
            print(f"Thank you, dear {key.title()} for taking the survey and choosing {value.title()} as your favorite language");

polling(favorite_languages);