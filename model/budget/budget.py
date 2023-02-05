"""
filename: budget.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class Budget
"""
import constants


class Budget:
    def __init__(self):
        self.__total_balance = constants.UNDEFINED_CLASS_FIELD
        self.__storage_outcomes = constants.UNDEFINED_CLASS_FIELD
        self.__salary_outcomes = constants.UNDEFINED_CLASS_FIELD
        self.__electricity_bills = constants.UNDEFINED_CLASS_FIELD
        self.__water_bills = constants.UNDEFINED_CLASS_FIELD
        self.__garbage_bills = constants.UNDEFINED_CLASS_FIELD  # to be constant
        self.__salon_incomes = constants.UNDEFINED_CLASS_FIELD
        self.__profit = constants.UNDEFINED_CLASS_FIELD

    def get_total_balance(self):
        return self.__total_balance

    def get_storage_outcomes(self):
        return self.__storage_outcomes

    def get_salary_outcomes(self):
        return self.__salary_outcomes

    def get_electricity_bills(self):
        return self.__electricity_bills

    def get_water_bills(self):
        return self.__water_bills

    def get_garbage_bills(self):
        return self.__garbage_bills

    def get_salon_incomes(self):
        return self.__salon_incomes

    def get_profit(self):
        return self.__profit

    def calculate_storage_outcomes(self):
        pass

    def calculate_salary_outcomes(self):
        pass

    def calculate_electricity_bills(self):
        pass

    def calculate_water_bills(self):
        pass

    def set_garbage_bills(self, new_garbage_bill):
        self.__garbage_bills = new_garbage_bill

    def calculate_salon_incomes(self):
        pass

    def calculate_profit(self):
        pass

    def update_total(self):
        pass
