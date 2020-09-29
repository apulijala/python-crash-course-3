"""
7-1. Rental Car: Write a program that asks the user what kind of rental car 
they would like. Print a message about that car, 
such as “Let me see if I can find you a Subaru.”
"""


def rental_car():
    rental_car = input(f"What kind of car would you like to drive? ")
    print(f"I would like to drive {rental_car}")



"""
7-2. Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group. If the answer is more than eight, 
print a message saying they’ll have to wait for a table. Otherwise, 
report that their table is ready.
"""

def restaurant_setting():
    numpeople = input(f"Enter the number of people in a table : ")
    numpeople = int(numpeople)
    if numpeople > 8: 
        print("Users will have to wait for the table")
    else: 
        print("Table is ready")

"""
7-3. Multiples of Ten: 
Ask the user for a number, and then report whether the number 
is a multiple of 10 or not.
"""

def multiples_of_10():
    number = input(f"Enter a number ? ")
    if number % 10 == 0: 
        print(f"{number} is a multiple of 10")
    else: 
        print(f"{number} is not a multiple of 10")


