"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an 
attribute called number_served with a default value of 0. Create an instance called
 restaurant from this class. 
Print the number of customers the restaurant has served, and then change this 
value and print it again.
Add a method called set_number_served() that lets you set the number of customers 
that have been served. Call this method with a new number and print the value again.
"""

class Restaurant():
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine = cuisine
        self.numserved = 0
        
        
    def set_number_served(self, numcustomers):
        self.numserved = numcustomers
        
    def increment_number_served(self, incnumber):
        self.numserved = self.numserved + incnumber 
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves food of type {self.cuisine}")
        
    
    def get_number_served(self):
        return self.numserved
"""
Add a method called increment_number_served() that lets you increment the number of customers 
who’ve been served. Call this method with any number you like that could represent 
how many customers were served in, say, a day of business.
"""

"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class from 
Exercise 9-3 (page 162). Write a method called increment_login_attempts() that increments 
the value of login_attempts by 1. Write another method called 
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly, and 
then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
Unlike java there is more than one class in Python. 
"""

class User():
    def __init__(self, first_name, last_name):
        self.user_profile = {}
        self.user_profile["firstname"] = first_name
        self.user_profile["lastname"] = last_name
        self.user_profile["login_atempts"] = 0
        
    def reset_login_attempts(self):
        self.user_profile["login_atempts"] = 0
    
    def increment_login_attempts(self, increment):
        self.user_profile["login_atempts"] += increment
        
    def desribe_user(self):
        return self.user_profile
        
