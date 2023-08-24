""" with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read();
print(contents.rstrip());

file_path = '/Users/terranceford/Downloads/code_v2023-04-07/kms/ExampleSecretFile.txt';
with open(file_path) as file_object:
    contents = file_object.read();
print(contents.rstrip());
#wow that worked

filename = 'text_files/pi_digits.txt';
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip());
with open(filename) as file_object:
    lines = file_object.readlines();

pi_string = '';
for line in lines:
    pi_string += line.strip();

print(pi_string, f"\n{len(pi_string)}");

for line in lines:
    print(line.rstrip()); """

def one_million_lines():
    filename = 'text_files/pi_million_digits.txt';
    with open(filename) as file_object:
        lines = file_object.readlines();
    pi_string = '';
    for line in lines: 
        pi_string += line.strip();
    print(f"{pi_string[:52]}...")
    print(f"The length of the string is {len(pi_string)}");

#one_million_lines();

def birthday_pi():
    filename = 'text_files/pi_million_digits.txt';
    with open(filename) as file_object:
        lines = file_object.readlines();
    pi_string = '';
    for line in lines: 
        pi_string += line.strip();
    birthday = input("Enter your birthday in mmddyy format:");
    if birthday in pi_string:
        print("Your birth is in the first one million digits of pi. This info means nothing");
    else:
        print("Your birthday is not in the first one million digits of pi.")

#birthday_pi();

def create_txt(method):
    filename = 'programming.txt';
    with open(filename, f"{method}") as file_object:
        file_object.write("Take a shot for me\n");
        file_object.write("(oh-oh-oh-oh, oh-oh-oh-oh)\n");

#create_txt("w"); #write/create file
#create_txt("a"); #append/add to file

def divide_by_zero():
    print("Give me two numbers, and I'll divide them.\nEnter 'q' to quit");
    while True:
        first_number = input("\nFirst number: ");
        if first_number.lower() == 'q':
            break;
        second_number = input("Second number: ");
        if second_number.lower() == 'q':
            break;
        try:
            answer = int(first_number) / int(second_number);
        except ZeroDivisionError:
            print("You CAN NOT divide by 0 NOR can you divide LETTERS!");
        except ValueError:
            print("You CAN NOT divide by 0 NOR can you divide LETTERS!");
        else:
            print(answer);

#divide_by_zero();
#filename = "chapter_10/text_files/learning_python.txt";
def num_of_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read();
    except FileNotFoundError:
        #pass -failing silently
        print(f"Sorry, the file {filename} does not exist.");
    else:
        words = contents.split();
        num_words = len(words);
        print(f"The file {filename} has about {num_words} words.\n");

def count_multiple_files(files_list):
    filenames = files_list;
    for filename in filenames:
        num_of_words(filename);

count_multiple_files(["chapter_10/text_files/learning_python.txt", "chapter_10/text_files/pi_digits.txt", "chapter_10/text_files/pi_million_digits.txt", "chapter_10/text_files/programming_poll.txt"]);