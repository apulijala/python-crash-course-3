from restaurant import  * # Restaurant as Restaurant
import unittest


class RestaurantTest(unittest.TestCase):
    # Method should be called as test
    def test_restaurant(self):
        restaurant = Restaurant("Llandysul Taj", "Indian Cuisine")
        restaurant.describe_restaurant()  
        
    def test_dog_behaviour(self):
        dog = Dog("Willie", 36)
        dog.sit()

    def test_user(self):
        user = User("Arvind", "Pulijala")
        user.increment_login_attempts(8)
        print(user.desribe_user())






if __name__ == "__main__":
    unittest.main()
