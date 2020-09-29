import unittest
from city_country import * 

class CityCountryTester(unittest.TestCase):
    def test_city_country(self):
        citycountry = city_country(country="Wales", city="Carmarthen")
        self.assertEqual(citycountry, "Carmarthen, Wales")
        
        citycountry = city_country(country="Paris'O'London", city="Carmarthen")
        self.assertEqual(citycountry, "Carmarthen, Paris'O'London")
    
    def test_city_country_population(self):
        citycountry = city_country_population(country="Wales", city="Carmarthen",population=10000)
        self.assertEqual(citycountry, "Carmarthen, Wales - population 10000")
        
        citycountry = city_country_population(country="Paris'O'London", city="Carmarthen", population=50000)
        self.assertEqual(citycountry, "Carmarthen, Paris'O'London - population 50000")
        
        citycountry = city_country_population("Santiago", "Chile")
        self.assertEqual(citycountry, "Santiago, Chile")

if __name__ == "__main__":
    unittest.main()
