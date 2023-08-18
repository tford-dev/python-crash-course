"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you
invite? Make a list that includes at least three people you’d like to invite to dinner. Then use
your list to print a message to each person, inviting them to dinner.
"""
guest_list = ['coach greg adams', 'aaron clarey', 'myron gaines'];
guest_list_extended = ['jon zherka', 'rich cooper', 'justin waller']

def dinner_invite(list_arr, list_arr_1):
    print(f"Of course, {list_arr[2].title()} can't make it.")
    del list_arr[2];
    list_arr.insert(1, "kevin samuels")
    print("I have obtained a bigger dinner table, I shall invite more guests! \nbut I only have 2 seats actually...");
    list_arr.insert(0, list_arr_1[0]);
    list_arr.insert(2, list_arr_1[1]);
    list_arr.append(list_arr_1[2]);
    for guest in reversed(list_arr):
        if len(list_arr) != 2:
            list_arr.pop();
            print(f"{guest.title()}, \nI have less space than planned so don't come.");
    for guest_left in list_arr:
        print(f"{guest_left.title()}, \nYou are invited to throw down on some food in my home.");

dinner_invite(guest_list, guest_list_extended);

def clear_list(list_arr):
    del list_arr[:];
    print(guest_list);

clear_list(guest_list);

"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so
you need to send out a new set of invitations. You’ll have to think of someone else to invite.
Start with your program from Exercise 3-4. Add a print() call at the
end of your program stating the name of the guest who can’t make
it.
Modify your list, replacing the name of the guest who can’t make
it with the name of the new person you are inviting.
Print a second set of invitation messages, one for each person who
is still in your list.
"""

"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think
of three more guests to invite to dinner.
Start with your program from Exercise 3-4 or Exercise 3-5. Add a
print() call to the end of your program informing people that you
found a bigger dinner table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your
list.
"""

"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time
for the dinner, and you have space for only two guests.
Start with your program from Exercise 3-6. Add a new line that
prints a message saying that you can invite only two people for
dinner.
"""

"""
Use pop() to remove guests from your list one at a time until only
two names remain in your list. Each time you pop a name from
your list, print a message to that person letting them know you’re
sorry you can’t invite them to dinner.
Print a message to each of the two people still on your list, letting
them know they’re still invited.
Use del to remove the last two names from your list, so you have
an empty list. Print your list to make sure you actually have an
empty list at the end of your program.
"""