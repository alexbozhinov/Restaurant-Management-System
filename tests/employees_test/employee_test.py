"""
filename: employee_test.py
author: alexbozhinov
created: 18.01.2023
purpose: definition of class Employee unittests
"""

import unittest

from model.employees.employee import Employee


class EmployeeTest(unittest.TestCase):

    def test_employee_name(self):
        emp_1 = Employee('Aleks Veselinov Bozhinov', '0123456789')
        emp_2 = Employee()

        self.assertEqual(emp_1.get_name(), 'Aleks Veselinov Bozhinov')
        self.assertEqual(emp_2.get_name(), 'UNDEFINED')

    def test_employee_identification_number(self):
        emp_1 = Employee('Aleks Veselinov Bozhinov', '0123456789')
        emp_2 = Employee('Ivan Ivanov Dimitrov')

        self.assertEqual(emp_1.get_identification_number(), '0123456789')
        self.assertEqual(emp_2.get_identification_number(), 'UNDEFINED')

    def test_employee_email(self):
        emp_1 = Employee('Aleks Veselinov Bozhinov', '0123456789')
        emp_2 = Employee('Ivan Ivanov Dimitrov')

        self.assertEqual(emp_1.get_email(), 'aleks_bozhinov@emp.com')
        self.assertEqual(emp_2.get_email(), 'ivan_dimitrov@emp.com')

    def test_employee_salary(self):
        emp_1 = Employee('Aleks Veselinov Bozhinov', '0123456789')
        emp_2 = Employee('Ivan Ivanov Dimitrov')

        self.assertEqual(emp_1.get_salary().get_money(), '0.00 лв')

        emp_1.set_salary('900.00')
        self.assertEqual(emp_1.get_salary().get_money(), '900.00 лв')

        emp_2.set_salary('1000.00')
        self.assertEqual(emp_2.get_salary().get_money(), '1000.00 лв')

        emp_2.update_salary(10)
        self.assertEqual(emp_2.get_salary().get_money(), '1100.00 лв')


if __name__ == '__main__':
    unittest.main()
