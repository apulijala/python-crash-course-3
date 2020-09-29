import unittest
from more_tests import *
from alien_colors import *  

class TestBooleanOperators(unittest.TestCase):
    # Method name has to start with test to make this work.
        def test_store_single_response(self):
            test_result = equality_inequality_test("hello", "hello")
            self.assertTrue(test_result)
            test_result = equality_inequality_test("hello", "world")
            self.assertFalse(test_result)
            
        def test_lower_string_comparision(self):
            test_result = lower_string_comparision("datta", "DATTA")
            self.assertTrue(test_result)
            test_result = equality_inequality_test("hello", "WORLD")
            self.assertFalse(test_result)
            

        def test_numerical_values_equal(self):
            self.assertTrue(numerical_values_equal(8, 8))


        def test_numerical_values_greater(self):
            self.assertTrue(numerical_values_greater(10, 8))

        def test_numerical_values_lesser(self):
            self.assertTrue(numerical_values_lesser(6, 8))
            
        def test_using_and_keyword(self):
            andresult = using_and_keyword(12, "laLItha")
            self.assertTrue(andresult)
            andresult = using_and_keyword(20, "digambara")
            self.assertFalse(andresult)
        

        def test_using_or_keyword(self):
            orresult = using_or_keyword("myword", "myword")
            self.assertTrue(orresult)
            orresult = using_or_keyword("MyWord", "MYWord")

        def test_alien_colors(self):
            alien_points = alien_colors("blue")
            self.assertEqual(alien_points, 5)

            alien_points = alien_colors("Blue")
            self.assertEqual(alien_points, 5)

            alien_points = alien_colors("bLuE")
            self.assertEqual(alien_points, 5)

            alien_points = alien_colors("yellow")
            self.assertEqual(alien_points, None)


        def test_alien_if_else(self):
            alien_points = alien_colors("yellow")
            self.assertEqual(alien_points, None)

        def test_alien_colors_modified(self):
            new_modified = alien_colors_modified("GREEN")
            self.assertEqual(new_modified, 5)

            new_modified = alien_colors_modified("Red")
            self.assertEqual(new_modified, 10)

            failing_colors = ["Ornage", "Magento", "Blue"]
            for color in failing_colors:
                alien_points = alien_colors_modified_if_else(color)
                self.assertIsNone(alien_points)

        def test_alien_colors_modified(self):
            color_mod = alien_colors_modified_if_else_with_hash("greEn")
            self.assertEqual(color_mod, 5)

        def test_alien_colors_modified(self):
            color_mod = alien_colors_modified_if_else_with_hash("greEn")
            self.assertEqual(color_mod, 5)

            color_mod = alien_colors_modified_if_else_with_hash("YELLOW")
            self.assertEqual(color_mod, 10)

            color_mod = alien_colors_modified_if_else_with_hash("Red")
            self.assertEqual(color_mod, 15)

            color_mod = alien_colors_modified_if_else_with_hash("Magento")
            self.assertEqual(color_mod, None)

        def test_get_type_of_person_by_age_with_if(self):
            person_type = get_type_of_person_by_age_with_if(1)
            self.assertEqual(person_type, "baby")

            person_type = get_type_of_person_by_age_with_if(3)
            self.assertEqual(person_type, "toddler")

            person_type = get_type_of_person_by_age_with_if(13)
            self.assertEqual(person_type, "teenager")

            person_type = get_type_of_person_by_age_with_if(17)
            self.assertEqual(person_type, "teenager")

            person_type = get_type_of_person_by_age_with_if(18)
            self.assertEqual(person_type, "teenager")


            person_type = get_type_of_person_by_age_with_if(63)
            self.assertEqual(person_type, "adult")
            
            person_type = get_type_of_person_by_age_with_if(65)
            self.assertEqual(person_type, "elder")

            person_type = get_type_of_person_by_age_with_if(67)
            self.assertEqual(person_type, "elder")

        def test_favorite_fruits(self):
           ret_val = fruit_exists("bananas")
           self.assertEqual(ret_val, "You really like bananas")
        
           ret_val = fruit_exists("Oranges")
           self.assertEqual(ret_val, None)

        
# Triggers the test case. 
if __name__ == '__main__':
       unittest.main()

