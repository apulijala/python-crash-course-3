"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. 
Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

Write an if statement to test whether the alien’s color is green. If it is, print a message that the 
player just earned 5 points.
Write one version of this program that passes the if test and another that fails. 
(The version that fails will have no output.)

"""

def alien_colors(color):
    if color.upper() == "BLUE":
        return 5
    return None      


def alien_colors_modified(color):
    if color.upper() == "GREEN":
        return 5 
    else:
        return 10

"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 
into an if-elif-else chain.
If the alien is green, print a message 
that the player earned 5 points.
If the alien is yellow, print a message that 
the player earned 10 points.
If the alien is red, print a message that 
the player earned 15 points.
Write three versions of this program, making sure each message 
is printed for the appropriate color alien.
"""

def alien_colors_modified_if_else(color):
    if color.upper() == "GREEN":
        return 5
    elif color.upper() == "YELLOW":
        return 10
    elif color.lower() == "red":
        return 15
    
    return None

"""
    Learn git operations, otherwise 
    it will prevent you from doing work. 
"""

def alien_colors_modified_if_else_with_hash(color):
    colors = {
        "GREEN" : 5,
        "YELLOW" : 10,
        "RED" : 15
    }
    # to avodid the key error. 
    return colors.get(color.upper(), None)

"""
Write an if-elif-else chain that determines a person’s stage of life. 
Set a value for the variable age, and then:
If the person is less than 2 years old, 
print a message that the person is a baby.
If the person is at least 2 years old but less than 4, 
print a message that the person is a toddler.
If the person is at least 4 years old but less than 13, 
print a message that the person is a kid.
If the person is at least 13 years old but less than 20, 
print a message that the person is a teenager.
If the person is at least 20 years old but less than 65, 
print a message that the person is an adult.
If the person is age 65 or older, print a message that the person is an elder.
"""


def get_type_of_person_by_age_with_if(age):
    if age < 2:
        return "baby"
    elif age >= 2 and age < 4:
        return "toddler"
    elif age >= 4 and age < 13:
        return "kid"
    elif age >= 13 and age < 20:
        return "teenager"
    elif age >= 20 and age < 65:
        return "adult"
    elif age >= 65:
        return "elder"


def fruit_exists(fruit):
    my_fav_fruits = ["bananas", "oranges", "grapes"]
    if fruit in my_fav_fruits:
        return f"You really like {fruit}"
    else: 
        return None
