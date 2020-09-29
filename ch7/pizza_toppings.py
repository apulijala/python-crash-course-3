"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value. As they enter each topping, 
print a message saying you’ll add that topping to their pizza.
"""

def pizza_toppings_quit():
    topping = input("Enter Pizza topping or enter quit? ")
    toppings = []
    while topping.upper() != "QUIT":
        toppings.append(topping)
        topping = input("Enter Pizza topping or enter quit? ")
    
    for topping in toppings:
        print(f"I will be adding {topping} topping to the pizza")


"""
For Anna
7-5. Movie Tickets: A movie theater charges different ticket prices depending 
on a person’s age. 
If a person is under the age of 3, the ticket is free; if they are between 3 and 12, 
the ticket is $10; and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, and then tell them the
cost of their movie ticket.
"""

def movie_tickets():
    age = input("Enter Person's age or enter quit to terminate? ")
    age = int(age)
    more_ages = True
    while more_ages:
        if age < 3:
            print("Ticket : Free ")
        elif age >= 3 and age < 12:
            print("Ticket : $10")
        elif age >= 12:
            print("Ticket : $15")
        age = input("Enter Person's age or enter quit to terminate? ")
        if age.upper() == "QUIT":
            more_ages = False
        else: 
            age = int(age)

"""
7-6. Three Exits: Write different versions of either 
Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
Use a conditional test in the while statement to stop the loop.
Use an active variable to control how long the loop runs.
Use a break statement to exit the loop when the user enters a 'quit' value.
"""

def movie_tickets_quit_with_if():

    age = input("Enter Person's age or enter quit to terminate? ")
    age = int(age)
    more_ages = True
    while more_ages:
        if age < 3:
            print("Ticket : Free ")
        elif age >= 3 and age < 12:
            print("Ticket : $10")
        elif age >= 12:
            print("Ticket : $15")
        age = input("Enter Person's age or enter quit to terminate? ")
        if age.upper() == "QUIT":
            break
          

"""
7-7. Infinity: Write a loop that never ends, and run it. 
(To end the loop, press CTRL-C or close the window displaying the output.)
"""
