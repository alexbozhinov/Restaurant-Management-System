"""
filename: waiter.py
author: alexbozhinov
created: 19.01.2023
purpose: definition of class Waiter, which inherits Employee
"""
from model.employees.employee import Employee


class Waiter(Employee):
    def __init__(self, name, identification_number):
        super().__init__(name, identification_number)
        self._tables = []
        self._number_of_tables = 0
        self._number_of_orders = 0

    def get_tables(self):
        return self._tables

    def get_number_of_tables(self):
        return self._number_of_tables

    def get_number_pf_orders(self):
        return self._number_of_orders

    def create_order(self):
        pass

    def edit_order(self):
        pass

    def cancel_order(self):
        pass

    def finish_order(self):
        pass

    def reserve_table(self):
        pass

    def cancel_table_reservation(self):
        pass

    def release_receipt(self):
        pass

    def print_receipt(self):
        pass


# manual tests
w = Waiter('Konstantin Ivanov Dimitrov', '5555566666')
print(w)
