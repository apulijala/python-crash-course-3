import unittest
from restaurant_with_served import * 

# Named the testing class as Restaurnt. 
class RestaurantTest(unittest.TestCase):
    def test_restaurant(self):
        r = Restaurant("Taj Mahal", "Chicken Cuisine")
        r.describe_restaurant()
        r.increment_number_served(7)
        num_served = r.get_number_served()
        print(f"{r.restaurant_name} has served {num_served} customers")
        
    
    def test_user(self):
        user = User("Arvind", "Puljala")
        user.increment_login_attempts(19)
        userprofile = user.desribe_user()
        print(userprofile)
        user.reset_login_attempts()
        userprofile = user.desribe_user()
        print(userprofile)
        

if __name__ == "__main__":
    unittest.main()
