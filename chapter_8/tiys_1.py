"""
8-7. Album: Write a function called make_album() that builds a dictionary describing a music
album. The function should take in an artist name and an album title, and it should return a
dictionary containing these two pieces of information. Use the function to make three
dictionaries representing different albums. Print each return value to show that the dictionaries
are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number
of songs on an album. If the calling line includes a value for the number of songs, add that value
to the album’s dictionary. Make at least one new function call that includes the number of
songs on an album

8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows
users to enter an album’s artist and title. Once you have that information, call make_album()
with the user’s input and print the dictionary that’s created. Be sure to include a quit value in
the while loop.

"""
def process_terminated():
    print("Proccess terminated.");

def make_album(a_name, a_title, num_of_tracks=None):
    if num_of_tracks:
        album_dict = {"artist name" : a_name, "album title" : a_title, "number of tracks" : num_of_tracks};
        return (f"The artist that 'made' the album {(album_dict['album title']).title()} is {(album_dict['artist name']).title()}. This album has {(album_dict['number of tracks'])} tracks.")
    else: 
        album_dict = {"artist name": a_name, "album title": a_title};
        return (f"The artist that 'made' the album {(album_dict['album title']).title()} is {(album_dict['artist name']).title()}.")

def user_albums():
    while True:
        print("Please, enter an artist name and the title of an album of theirs. \nNot Taylor Swift, please and thank you.");
        print("Enter 'q' at any time to terminate this process.");
        artist_name = input("Artist name: ");
        if(artist_name.lower() == 'q'):
            process_terminated();
            break;
        album_title = input("Album title: ");
        if (album_title.lower() == 'q'):
            process_terminated();
            break
        print("Please enter the number of tracks on the album. \nIf you do not know or do not wish to enter the number of tracks, then enter 's' or simply press enter to skip.");
        number_of_tracks = input(f"Number of tracks for the album {album_title.title()} by {artist_name.title()}: ");
        if ((number_of_tracks.lower() == 's') or number_of_tracks.lower() == ''):
            number_of_tracks = None;
        elif (number_of_tracks == 'q'):
            process_terminated();
            break;
        album_dictionary = make_album(artist_name, album_title, number_of_tracks)
        print(album_dictionary);

user_albums(); 