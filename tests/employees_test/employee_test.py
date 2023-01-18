"""
filename: employee_test.py
author: alexbozhinov
created: 18.01.2023
purpose: definition of class employee unittests
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


if __name__ == '__main__':
    unittest.main()



