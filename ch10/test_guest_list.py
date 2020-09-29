import unittest
from guest_list import * 

class GuestListTester(unittest.TestCase):
    
    def setUp(self):
        self.filename = "guest.txt"
        self.guest = Guest("guest.txt")
    
    @unittest.skip
    def test_prompt_user(self):
        self.guest.prompt_user()
        
    @unittest.skip
    def test_guest_book(self):
        self.guest.guest_book()
    
    def test_programming_poll(self):
        filename = "programming.txt"
        guest = Guest(filename)
        guest.programming_poll()



if __name__ == "__main__":
    unittest.main()
