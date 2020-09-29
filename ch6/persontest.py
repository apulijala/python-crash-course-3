import person
from person import *
import unittest

class PersonTest(unittest.TestCase):

    
    def test_store_person(self):
        person = store_person("Arvind", "Pulijala", 34, "London")
        self.assertEqual(person.get("first"), "Arvind")

    def test_store_favorite_number(self):
        favorite_numbers()

    def test_glossary(self):
        meanings = glossary()
        for idiom, meaning in meanings.items():
            print(f"{idiom} is {meaning}")

    def test_rivers_information(self):
        rivers_information()

    def test_favorite_languages(self):
        taken_not_taken = favorite_languages()
        print(taken_not_taken.get("taken"))
        print(taken_not_taken.get("not_taken"))


    def test_people(self):
        people()

    def test_pets(self):
        pets()

    def test_fav_places(self):
        fav_places()

    def test_fav_nums(self):
        fav_numbers()

    def test_cities(self):
        cities()


    


if __name__ == '__main__':
       unittest.main()
