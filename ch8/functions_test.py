import unittest
from functions import * 

class tshirt_tester(unittest.TestCase):

    def test_user_album_input(self):
        make_user_album()

if __name__ == "__main__":
    unittest.main()
