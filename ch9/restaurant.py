"""
9-1. Restaurant: Make a class called Restaurant. 
The __init__() method for Restaurant should store two attributes: a restaurant_name and a 
cuisine_type. Make a method called describe_restaurant() that prints 
these two pieces of information, and a method called open_restaurant() 
that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. 
Print the two attributes individually, and then call both methods.
"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is serving {self.cuisine_type}")


class Dog:
    # this is consturctor and should be passed self. """Initialize name and age attributes."""
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def sit(self):
		 print(f"{self.name} is now sitting.")
        