"""
10-6. Addition: One common problem when prompting for numerical input occurs when
people provide text instead of numbers. When you try to convert the input to an int, you’ll get
a ValueError. Write a program that prompts for two numbers. Add them together and print
the result. Catch the ValueError if either input value is not a number, and print a friendly error
message. Test your program by entering two numbers and then by entering some text instead
of a number.
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user
can continue entering numbers even if they make a mistake and enter text instead of a number.
"""
def add_num():
    print("Peace Be Upon You. Enter 2 numbers to add.\nEnter 'q' to quit");
    while True:
        first_num = input("First number to add: ");
        if first_num.lower() == 'q':
            break;
        second_num = input("Second number to add: ");
        if second_num.lower() == 'q':
            break;
        try:
            answer = int(first_num) + int(second_num);
        except ValueError:
            print("Please enter numbers to add, no letters or special numbers.")
        else:
            print(answer);
#add_num();

"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in
the first file and three names of dogs in the second file. Write a program that tries to read these
files and print the contents of the file to the screen. Wrap your code in a try-except block to
catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the
files to a different location on your system, and make sure the code in the except block
executes properly.
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if
either file is missing.
"""
def cats_and_dogs():
    filename_list = ["chapter_10/text_files/cats.txt", "chapter_10/tex_files/dogs.txt"];
    for filename in filename_list:
        try: 
            with open(filename, encoding='utf-8') as file_object:
                for line in file_object:
                    print(line.rstrip());
        except FileNotFoundError:
            #pass; fail silently if either file is missing
            print(f"{filename} is not found. Sorry!");

#cats_and_dogs();

"""
10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/) and find a few texts
you’d like to analyze. Download the text files for these works, or copy the raw text from your
browser into a text file on your computer.
"""
def common_words(filepath, str_lookup):
    word_count = 0;
    with open(filepath) as file_object:
        lines = file_object.readlines();
        for line in lines:
            word_count += line.lower().count(str_lookup.lower());
    print(f"The word '{str_lookup}' shows up {word_count} times in: \n{filepath}.");

common_words("chapter_10/text_files/crew_love.txt", "crew");