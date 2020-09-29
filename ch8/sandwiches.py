"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, 
and it should print a summary of the sandwich that’s being ordered. Call the function three times, 
using a different number of arguments each time.
"""

def items_on_sandwich(*toppings):
    for topping in toppings:
        print(f"I have added a topping called {topping}")

"""
8-13. User Profile: Start with a copy of user_profile.py from page 149. 
Build a profile of yourself by calling build_profile(), using your first and 
last names and three other key-value pairs that describe you.
"""
def user_profile(first, last, **userprofile):
    userprofile["first"] = first
    userprofile["last"] = last
    return userprofile

"""
8-14. Cars: Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. 
It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, 
such as a color or an optional feature. Your function should work for a call like this one:
"""

def make_car(manufacturer, model, **other_features):
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model

    for type, feature in other_features.items():
        car[feature] = feature
    
    return car





