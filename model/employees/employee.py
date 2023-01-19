"""
filename: employee.py
author: alexbozhinov
created: 18.01.2023
purpose: definition of class employee
"""
import constants
import bcrypt

from model.employees.money import Money
from decimal import Decimal


class Employee:
    def __init__(self, name=constants.UNDEFINED_CLASS_FIELD, identification_number=constants.UNDEFINED_CLASS_FIELD):
        self._name = name
        self._identification_number = identification_number
        self._password = constants.UNDEFINED_CLASS_FIELD
        self._username = constants.UNDEFINED_CLASS_FIELD
        self._salary = Money()
        self._email = self.__generate_email()

    def get_name(self):
        return self._name

    def get_identification_number(self):
        return self._identification_number

    def get_email(self):
        return self._email

    def get_username(self):
        return self._username

    def get_salary(self):
        return self._salary

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_salary(self, salary):
        self._salary = Money(salary)

    def update_salary(self, percentage):
        if percentage > Decimal(0.0) or percentage <= Decimal(100.0):
            new_salary = (self._salary.get_value() * percentage) / Decimal(100.0) + self._salary.get_value()

        self.set_salary(new_salary)

    def hash_password(self):
        # Adding the salt to password
        salt = bcrypt.gensalt()
        # Hashing the password
        hashed_password = bcrypt.hashpw(self._password, salt)
        return hashed_password

    def __generate_email(self):
        names = self._name.lower().split()
        return '{}_{}@{}.com'.format(names[0], names[-1], constants.SHORT_RESTAURANT_NAME)

    # implemented for manual tests
    def __str__(self):
        return 'Employee name: {}, idn: {}, usr: {}, psw: {}, email: {}'\
            .format(self._name, self._identification_number, self._username, self._password, self._email)


# manual test
"""
e = Employee("Aleks Veselinov Bozhinov", "0123456789")
e.set_username('abozhinov')
e.set_password('0000000000')
print(e)
"""
