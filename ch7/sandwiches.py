from typing import List, Set, Dict, Tuple, Optional

"""
7-8. Deli: Make a list called sandwich_orders and fill it with 
the names of various sandwiches.
 Then make an empty list called finished_sandwiches. 
Loop through the list of sandwich orders and print a message for each order, 
such as I made your tuna sandwich. 
As each sandwich is made, move it to the list of finished sandwiches. 
After all the sandwiches have been made, 
print a message listing each sandwich that was made.
"""

def make_sandwiches(sandwiches):

    finished_sandwiches = []
    for sandwich in sandwiches:
        print(f"I have made you a {sandwich} sandwich")
        finished_sandwiches.append(sandwich)
    return finished_sandwiches


"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, 
make sure the sandwich 'pastrami' appears in the list at least three times. 
Add code near the beginning of your program to print a message saying the deli has run out 
of pastrami, and then use a while loop to remove all occurrences of 'pastrami' 
from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

def no_pastrami(sandwiches_pastrami):
    print(f"Deli has run out of Patrami")
    while "pastrami" in sandwiches_pastrami:
        sandwiches_pastrami.remove("pastrami")
    print(sandwiches_pastrami)
    make_sandwiches(sandwiches_pastrami)

"""
7-10. Dream Vacation: Write a program that polls users about their dream vacation. 
Write a prompt similar to If you could visit one place in the world, 
where would you go? Include a block of code that prints the results of the poll.
"""

def dream_vacation():
    name = input("Enter the name or enter quit ? ")
    place = input("Which place would you like to visit or enter quit ? ")
    vactions = {}
    vactions[name] = place
    more_vacatons = False
    while(more_vacatons):
        name = input("Enter the name or enter quit ? ")
        if name.upper() == "QUIT":
            break
        place = input("Which place would you like to visit or enter quit ? ")
        if place.upper() == "QUIT":
            break
        
        vactions[name] = place

    
    print(vactions)

