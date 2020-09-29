def make_tshirt(size, msg):
    print(f"T-Shirt of size {size} Chanting {msg}")



"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default 
with a message that reads I love Python. Make a large shirt and a medium shirt with the 
default message, and a shirt of any size with a different message.
"""
def large_tshirt(mantra = "Jaya Guru Datta", size = "Large"):
    print(f"T-Shirt with mantra {mantra} of size {size}")


"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and 
its country. The function should print a simple sentence, 
such as Reykjavik is in Iceland. 
Give the parameter for the country a default value. Call your function for 
three different cities, at least one of which is not in the default country.
"""

def describe_city(city, country = "England"):
    msg = f"{city}, {country}"
    return msg


"""
8-7. Album: Write a function called make_album() that builds a dictionary 
describing a music album. The function should take in an artist name and 
an album title, and it should return a dictionary containing these 
two pieces of information. 

Use the function to make three dictionaries representing different albums. 
Print each return value to show that the dictionaries are storing the 
album information correctly.

Use None to add an optional parameter to make_album() that allows you to store 
the number of songs on an album. If the calling line includes a value 
for the number of songs, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of songs on an album.
"""

def make_albumn(artist="Arvind", title= "Lalitha Sahasranam", numSongs=None):
    album = {
        "artist" : artist,
        "title" : title
    }
    if numSongs != None:
        album["numsongs"] = numSongs
    
    return album

"""
8-8. User Albums: Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input 
and print the dictionary that’s created. Be sure to include a quit value in the while loop.
"""

def make_user_album():
    artist = input("Enter Artist Name or enter quit to quit: ")
    if artist.upper() == "QUIT":
        return
    title = input("Enter Title Name or enter quit to quit ")
    if title.upper() == "QUIT":
        return
    album = make_albumn(artist, title="Anagha Vratam")
    print("Album is ")
    print(album)
    morealbums = True
    while morealbums:
        artist = input("Enter Artist Name or enter quit to quit: ")
        if artist.upper() == "QUIT":
            # morealbums = False Not requires as user is not having input
            return
        title = input("Enter Title Name or enter quit to quit ")
        if title.upper() == "QUIT":
             # morealbums = False Not requires as user is not having input
            return
        album = make_albumn(artist, title)
        print(album)



