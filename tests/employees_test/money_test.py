"""
filename: employee_test.py
author: alexbozhinov
created: 18.01.2023
purpose: definition of class employee unittests
"""

import unittest

from model.employees.money import Money
from decimal import Decimal


class MoneyTest(unittest.TestCase):
    def test_money(self):
        m1 = Money('4.50')
        m2 = Money('50.00')
        m3 = Money()

        self.assertEqual(m1.get_money(), '4.50 лв')
        self.assertEqual(m2.get_money(), '50.00 лв')
        self.assertEqual(m3.get_money(), '0.00 лв')

    def test_value(self):
        m1 = Money('4.50')
        m2 = Money('50.00')
        m3 = Money()

        self.assertEqual(m1.get_value(), Decimal('4.50'))
        self.assertEqual(m2.get_value(), Decimal('50.00'))
        self.assertEqual(m3.get_value(), Decimal('0.00'))

    def test_currency(self):
        m1 = Money('50.00')
        m2 = Money()

        self.assertEqual(m1.get_currency(), 'лв')
        self.assertEqual(m2.get_currency(), 'лв')


if __name__ == '__main__':
    unittest.main()
