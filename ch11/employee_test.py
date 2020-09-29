from employee import *
import unittest 

class EmployeeTester(unittest.TestCase):
    def test_give_default_raise(self):
        employee = Employee("Arvind", "Pulijala", 10000) 
        employee.giveRaise()
        self.assertEqual(employee.getSalary(), 15000)
    
    def test_give_custom_raise(self):
        employee = Employee("Arvind", "Pulijala", 10000) 
        employee.giveRaise(7000)
        self.assertEqual(employee.getSalary(), 17000)
    

if __name__ == "__main__":
    unittest.main()
