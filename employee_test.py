from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Michael","Lee",200000)      
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 205000)

    def test_give_custom_raise(self):
        self.employee.give_raise(50000)
        self.assertEqual(self.employee.annual_salary, 250000)

if __name__ == "__main__":
    unittest.main()