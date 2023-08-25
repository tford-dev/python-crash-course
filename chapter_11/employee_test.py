import unittest;
from employee import Employee;

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee("terry", "stylez", 800000);

    def test_give_default_raise(self):
        salary = self.my_employee.give_raise();
        self.assertEqual(salary, 'Employee Terry Stylez has a salary of $805000.');

    def test_give_custom_raise(self):
        salary = self.my_employee.give_raise(100000)
        self.assertEqual(salary, 'Employee Terry Stylez has a salary of $900000.')

if __name__ == '__main__':
    unittest.main();