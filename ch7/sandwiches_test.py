from sandwiches import *
import unittest

class SandichTester(unittest.TestCase):

    @unittest.skip
    def test_make_sandwiches(self):
        sandwiches = ["Tomato", "Cheese", "Pepporoni", "Pineapple"]
        finished_sandwiches =   make_sandwiches(sandwiches)
        # sandwiches.append("Grapes")
        self.assertEqual(sandwiches, finished_sandwiches)

    @unittest.skip
    def test_make_no_pastrami(self):
        sandwiches = ["pastrami", "Tomato", "Cheese","Pastrami", "Pepporoni", "Pineapple", "Pastrami", "pastrami"]
        no_pastrami(sandwiches)

    
    def test_dream_vacation(self):
        dream_vacation()


if __name__ == "__main__":
    unittest.main()
