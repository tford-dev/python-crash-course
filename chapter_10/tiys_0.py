"""
10-1. Learning Python: Open a blank file in your text editor and write a few lines
summarizing what you’ve learned about Python so far. Start each line with the phrase In Python
you can. . .. Save the file as learning_python.txt in the same directory as your exercises from this
chapter. Write a program that reads the file and prints what you wrote three times. Print the
contents once by reading in the entire file, once by looping over the file object, and once by
storing the lines in a list and then working with them outside the with block.
"""
#once by reading in the entire file
def read_entire_file(filepath):
    with open(filepath) as file_object:
        contents = file_object.read();
    print(contents.rstrip());

#read_entire_file('text_files/learning_python.txt');

#once by looping over the file object
def read_by_loop(filepath):
    with open(filepath) as file_object:
        for line in file_object:
            print(line.rstrip());

#read_by_loop('text_files/learning_python.txt');

#once by storing the lines in a list and then working with them outside the with block

def read_by_list(filepath):
    with open(filepath) as file_object:
        lines = file_object.readlines();
    loop_string = "";
    for line in lines:
        loop_string += (f"\n{line.strip()}");
    print(loop_string);
    
#read_by_list('text_files/learning_python.txt');

"""
10-2. Learning C: You can use the replace() method to replace any word in a string with a
different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:
"""
def replace_word(filepath, str_lookup, str_replace):
    with open(filepath) as file_object:
        lines = file_object.readlines();
    txt_file_str = '';
    for line in lines:
        txt_file_str += (f"\n{line.strip()}");
    if str_lookup in txt_file_str:
        txt_file_str = txt_file_str.replace(str_lookup, str_replace);
        print(txt_file_str);
    else:
        print("The text you are looking to replace is not in this file.");

#replace_word('text_files/learning_python.txt', 'Take a shot for me', 'OVO and that XO! Bring it back!');