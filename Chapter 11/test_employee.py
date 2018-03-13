import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('Hugo', 'Chan', 1000)
        
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 6000)
        
    def test_give_custom_raise(self):
        self.my_employee.give_raise(4000)
        self.assertEqual(self.my_employee.annual_salary, 5000)
        
unittest.main()
