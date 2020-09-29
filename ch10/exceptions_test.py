import unittest
from jsondumps import *
from exceptions import * 


class AdditionTester(unittest.TestCase):
    
    def setUp(self):
        self.addition = Addition()
        self.catsanddogs = CatsAndDogs("cats.txt", "dogs.txt")
    
    @unittest.skip
    def test_addition(self):
        self.addition.add_numbers()
    
    @unittest.skip
    def test_add_numbers_while_loop(self):
        self.addition.add_numbers_while_loop() 
       
    @unittest.skip
    def test_add_cats_and_dogs(self):
        print("Dogs and Cats\n")
        self.catsanddogs.getCatsFile()
        self.catsanddogs.getDogsFile()
    
    @unittest.skip
    def test_common_words(self):
        """
        text = "TO Hell with You"
        print("\n")
        print(f"{text.lower()}")        
        """   
        filename = "gutenberg.txt"
        commonwords = CommonWords(filename)
        word = "the "
        count = commonwords.word_count(word)
        print("\n")
        print(f"{word} exists {count} times")
    
    def test_write_favorite_data_structures(self):
        jsondump = JsonDumps("myfile.txt")
        # jsondump.write_favorite_data_structures()
        jsondump.read_favorite_data_structure()

    

if __name__ == "__main__":
    unittest.main()
