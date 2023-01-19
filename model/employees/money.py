"""
filename: money.py
author: alexbozhinov
created: 19.01.2023
purpose: definition of class money
"""

from currencies import Currency
from decimal import Decimal
import constants


class Money:
    def __init__(self, value=constants.UNDEFINED_MONEY_VALUE):
        self.__value = Decimal('{}'.format(value))
        self.__currency = Currency(constants.CURRENCY)

    def set_value(self, value):
        self.__value = value

    def get_currency(self):
        return self.get_money().split()[-1]

    def get_value(self):
        return self.__value

    def get_money(self):
        return self.__currency.get_money_format('{}'.format(self.__value))
