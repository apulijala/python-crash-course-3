from restaurant_with_served import * 
""" 
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
Write a class called IceCreamStand that inherits from the Restaurant class 
you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). 
Either version of the class will work; just pick the one you like better. 
Add an attribute called flavors that stores a list of ice cream flavors. 
Write a method that displays these flavors. 
Create an instance of IceCreamStand, and call this method.
"""

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        
    def get_flavors(self):
        return self.flavors

"""
9-7. Admin: An administrator is a special kind of user. 
Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 
(page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, 
that stores a list of strings like "can add post", "can delete post", "can ban user", 
and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. 
Create an instance of Admin, and call your method.
"""
class Admin(User):
   def __init__(self, first_name, last_name, privileges):
       super().__init__(first_name, last_name)
       self.attributes = Privileges(privileges)
    
    
   def show_privileges(self):
       return self.attributes



"""
9-8. Privileges: Write a separate Privileges class. The class should have 
one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
Move the show_privileges() method to this class. 
Make a Privileges instance as an attribute in the Admin class. 
Create a new instance of Admin and use your method to show its privileges.
"""
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges
        
    
    def get_privileges(self):
        return self.privileges
