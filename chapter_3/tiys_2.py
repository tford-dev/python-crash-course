"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
Store the locations in a list. Make sure the list is not in alphabetical
order.
Print your list in its original order. Don’t worry about printing the
list neatly, just print it as a raw Python list.
Use sorted() to print your list in alphabetical order without
modifying the actual list.
Show that your list is still in its original order by printing it.
Use sorted() to print your list in reverse alphabetical order without
changing the order of the original list.
Show that your list is still in its original order by printing it again.
Use reverse() to change the order of your list. Print the list to show
that its order has changed.
Use reverse() to change the order of your list again. Print the list to
show it’s back to its original order.
Use sort() to change your list so it’s stored in alphabetical order.
Print the list to show that its order has been changed.
Use sort() to change your list so it’s stored in reverse alphabetical
order. Print the list to show that its order has changed.
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page
42), use len() to print a message indicating the number of people you are inviting to dinner.
"""

places = ["ibiza", "amsterdam", "singapore", "oregon", "wyoming"];
print(places);
print(sorted(places)); #sorts alphabetically without manipulating list
print(places);
print(sorted(places, reverse=True)); #sorts alphabetically in reverse without manipulating list
print(places);
print(places.reverse()); #sorts original list in reverse(or what it was last manipulated to in reverse)
print(places);
print(places.reverse()); #sorts list back to how it was if it was reversed previously
print(places);
print(places.sort()); #sorts alphabetically permanently
print(places);
print(len(places)); #length