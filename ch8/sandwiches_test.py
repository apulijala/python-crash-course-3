from sandwiches import items_on_sandwich, user_profile, make_car
import unittest

class SandwichTester(unittest.TestCase):
    
    def test_items_on_sandwhiches(self):
        items_on_sandwich("Tomato", "Cheese", "Pepperoni", "Pepper")
        items_on_sandwich(["Tomato", "Cheese"],["Pineapple", "Mango"])

    def test_user_profile(self):
        profile = \
            user_profile(last="Pulijala", first="Arvind",   \
            profession="AWS Engineer", doing="Learning Terraform")
        print(profile)

    def test_make_car(self):
        make_car("Honda", "Accord", type="solar", color="Red")
        

if __name__ == "__main__":
    unittest.main()
