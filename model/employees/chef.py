"""
filename: chef.py
author: alexbozhinov
created: 19.01.2023
purpose: definition of class Chef, which inherits Employee and StorageManager
"""
from model.employees.chef_type import ChefType
from model.employees.employee import Employee
from model.management.storage_manager import StorageManager


class Chef(Employee, StorageManager):
    def __init__(self, name: str, identification_number: str, chef_type=ChefType.CHEF_OWNER):
        super().__init__(name, identification_number)
        self._chef_type = chef_type
        self._meals_cocked = 0  # number of finished orders
        self._ingredient_orders_created = 0  # to deliver into the storage
        self._current_orders = 0  # to be coked

    def increase_meals_cocked(self, supplement=1):
        self._meals_cocked += supplement

    def increase_ingredient_orders_created(self, supplement=1):
        self._ingredient_orders_created += supplement

    def increase_current_orders(self, new_orders=1):
        self._current_orders += new_orders

    def decrease_current_orders(self, prepared_orders=1):
        if self._current_orders > 0:
            self._current_orders -= prepared_orders

    def promote_chef(self, new_chef_type: ChefType):
        self._chef_type = new_chef_type

    def get_chef_type(self):
        return self._chef_type

    def get_meals_cocked(self):
        return self._meals_cocked

    def get_ingredient_orders_created(self):
        return self._ingredient_orders_created

    def get_current_orders(self):
        return self._current_orders

    def start_next_order(self):
        pass

    def finish_order(self):
        pass

    def set_email(self, email):
        self._email = email

    def set_meals_cocked(self, meals_cocked):
        self._meals_cocked = meals_cocked

    def set_ingredient_orders_created(self, ingredient_orders_created):
        self._ingredient_orders_created = ingredient_orders_created

    def set_current_orders(self, current_orders):
        self._current_orders = current_orders


# manual tests
# c = Chef("Ivan Ivanov Ivanov", "1234567890")
# print(c)
