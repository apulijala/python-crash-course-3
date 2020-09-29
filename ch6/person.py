"""
6-1. Person: Use a dictionary to store information about a person you know. 
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city. 
Print each piece of information stored in your dictionary.
"""
def store_person(first, last, age, city):
    person = {
        "city" : city,
        "last" : last
    }

    person["first"] = first
    person["age"] = age
    return person

"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
Think of five names, and use them as keys in your dictionary. Think of a 
favorite number for each person, and store each as a value in your dictionary. Print 
each person’s name and their favorite number. For even more fun, poll a few friends and get
 some actual data for your program.
"""
def favorite_numbers():
    favnums = {
        "Andrew" : 3,
        "Prasanna" : 4,
        "Prasad" : 6
    }
    for name, num in favnums.items():
        print(f"{name}'s favorite number is {num}'")


"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
However, to avoid confusion, let’s call it a glossary.
Think of five programming words you’ve learned about in the previous chapters. Use 
these words as the keys in your glossary, and store their meanings as values.
Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, 
or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
"""
def glossary():
    
    meanings = {
     "if" : "If loop ends with if condition:", 
     "for" : "For loop",
     "next" : "next loop"
    }
    return meanings


"""
6-5. Rivers: Make a dictionary containing 
three major rivers and the country each river runs through. 
One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
Use a loop to print the name of each river included in the dictionary.
Use a loop to print the name of each country included in the dictionary.
"""

def rivers_information():

    rivers = {
        "Nile" : "Egypt", 
        "India" : "Ganges",
        "India" : "Yamuna"
    }
    print("Rivers and countries")
    for river, country in rivers.items():
        print(f"{river} runs through {country} ")

    print("Countries are: ")
    for river in rivers.values():
        print(f"{river}")

    
def favorite_languages():

    favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python'

       }

    list_of_people = ["jen","sarah"]
    not_taken = []
    taken = []

    for name in favorite_languages.keys():
        if name not in list_of_people:
            not_taken.append(name)
        else: 
            taken.append(name)
        
    return {
        "taken" : taken,
        "not_taken" : not_taken
    }



"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries 
representing different people, and store all three dictionaries in a list called people. 
Loop through your list of people. As you loop through the list, print everything you know about each person.
https://github.com/widdix/aws-ec2-ssh
6:50 AM started. 
"""

def people():
    person1 = store_person("Arvind", "Puljiala", 45, "Hyderabad")
    person2 = store_person("Ashwin", "Pulijala", 41, "Chicago")
    persons = []
    persons.append(person1)
    persons.append(person2)
    print(persons)

    print("Person List")
    for person in persons:
        print(f"First Name: {person['first']}")
        print(f"First Name: {person['last']}")
        print(f"First Name: {person['age']}")
        print(f"First Name: {person['city']}")


"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, 
include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
Next, loop through your list and as you do, print everything you know about each pet.
"""

def pets():
    pets = {
        "Tommy" : {
            "Owner" : "Arvind", 
            "Pet" : "Dog"
        }, 
        "Billy" : {
            "Owner" : "Ashwin", 
            "Pet" : "Cat"

        }
    }

    for pet in pets.keys():
        print(f"Pet Name: {pet}")
        print(f"Owner Name: {pets[pet]['Owner']}")
        print(f"Pet Type: {pets[pet]['Pet']}")

"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, 
and store one to three favorite places for each person. 
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
Loop through the dictionary, and print each person’s name and their favorite places.
"""

def fav_places():
    favorite_places = {
        "Arvind" : ["Llandysul", "Kasi", "Hyderabad"],
        "Ashwin" : ["Chicago", "Maine", "America"],
        "Andrew" : ["Ammanford", "Maine", "Phillipenes"]
    }

    for name in favorite_places.keys():
        print(f"{name}'s favorite places are :")
        for place in favorite_places.get(name, []):
            print(f"{place}")

"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite 
number. Then print each person’s name along with their favorite numbers.
"""

def fav_numbers():
    favaorite_nums = {
        "Andrew" : [66, 109, 1001],
        "Arvind" : [8, 5345, 333, 444, 6666],
        "Prasad" : [101, 1-6, 567, 108],
        "Prasanna" : [678, 899, 908, 76]
    }

    for name in favaorite_nums:
        print(f"{name}'s favorite numbers are: ")
        for number in favaorite_nums[name]:
            print(f"{number}")

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and include the country that the city is in, 
its approximate population, and one fact about that city. The keys for each city’s dictionary 
should be something like country, population, and fact. Print the name of each city and all of the 
information you have stored about it.
"""

def cities():
    cities = {
        "London" : {
            "Country" : "UK",
            "Popluation" : "30000000",
            "fact" : "Capital of England"
        }, 

        "Carmarthen" : {
            "Country" : "Wales",
            "Population" : "50,000",
            "fact" : "Near Skandavale"
        },

        "Paris" : {
            "Country" : "France",
            "Population" : "100,000",
            "fact" : "Capital of France"
        }
    }

    cities["Kasi"] : {
        "Country" : "India",
        "Population" : "200,000",
        "fact" : "In India"
    }


    for city in cities.keys():
        print(f"{city}'s details: ")
        # Not possible to have a key error. 
        for fact in cities[city]: # You are cat cities[city]
            print(f"{fact} : {cities[city][fact]}")

        print("==============")
    
    print("London's details")
    print(cities.get("London1"))









"""
6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
Use one of the example programs from this chapter, and extend it by adding new keys and values, 
changing the context of the program or improving the formatting of the output.
"""

   









