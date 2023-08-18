"""
8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function
called show_messages(), which prints each text message.
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a
function called send_messages() that prints each text message and moves each message to a
new list called sent_messages as it’s printed. After calling the function, print both of your lists
to make sure the messages were moved correctly.
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function
send_messages() with a copy of the list of messages. After calling the function, print both of
your lists to show that the original list has retained its messages.
"""

messages = [
    "hey, how are you?",
    "just checking in.",
    "wanna hang out later?",
    "what's up?",
    "see you soon!",
    "can't wait to see you.",
    "where are you now?",
    "thanks a bunch!"
];

sent_messages = [];

def show_messages(list_arr):
    for item in list_arr:
        print(f"{item}");

def send_messages(list_arr_from, list_arr_to):
    while list_arr_from:
        sent_message = list_arr_from.pop();
        print(f"Sending message: '{sent_message}'");
        list_arr_to.append(sent_message);
    print(f"List of messages to be sent: \n{list_arr_from}");
    print(f"List of messagrs that have been sent: \n{list_arr_to}");


# send_messages(messages, sent_messages);
#below I am sending a copy of the list using the [:] operator and then testing to see if the messages list kept it's integrity.
send_messages(messages[:], sent_messages)
print(messages);
print(sent_messages);