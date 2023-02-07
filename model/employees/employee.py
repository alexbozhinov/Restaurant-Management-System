"""
filename: employee.py
author: alexbozhinov
created: 18.01.2023
purpose: definition of class Employee
"""
import constants
import bcrypt

from model.employees.money import Money
from decimal import Decimal


class Employee:
    def __init__(self, name=constants.UNDEFINED_CLASS_FIELD, identification_number=constants.UNDEFINED_CLASS_FIELD):
        self._name = name

        if len(identification_number) == constants.BGN_IDENTIFICATION_NUMBER_LENGTH:
            self._identification_number = identification_number
        else:
            self._identification_number = constants.UNDEFINED_CLASS_FIELD

        self._password = constants.UNDEFINED_CLASS_FIELD
        self._username = self.__generate_username()
        self._email = self.__generate_email()
        self._salary = Money()

    """
    Accessor methods:
    """
    def get_name(self):
        return self._name

    def get_identification_number(self):
        return self._identification_number

    def get_email(self):
        return self._email

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_salary(self):
        return self._salary

    """
    Mutator methods:
    """
    def set_username(self, username: str):
        self._username = username

    def set_password(self, password: str):
        self._password = password

    def set_email(self, email):
        self._email = email

    def set_salary(self, salary: str):
        self._salary = Money(salary)

    """
    method purpose: update salary by given percentage
    """
    def update_salary(self, percentage: float):
        if percentage > Decimal(0.0) or percentage <= Decimal(100.0):
            new_salary = (self._salary.get_value() * percentage) / Decimal(100.0) + self._salary.get_value()
            self.set_salary(new_salary)

    """
    method purpose: hash password before putting it in the database table with bcrypt algorithm
    """
    def hash_password(self):
        # Adding the salt to password
        salt = bcrypt.gensalt()
        # Hashing the password
        hashed_password = bcrypt.hashpw(self._password.encode('utf-8'), salt)
        self._password = hashed_password

    """
    method purpose: checks if inputted password is equal with the hashed password in the database
    """
    def is_valid_password(self, password):
        if bcrypt.checkpw(str(password).encode('utf-8'), self._password):
            return True
        return False

    """
    method purpose: generating unique email of user, depending on their names and the short name of the restaurant
    future TODO: validate if names of employees duplicated, the email should be unique
    """
    def __generate_email(self):
        names = self._name.lower().split()
        return '{}_{}@{}.com'.format(names[0], names[-1], constants.SHORT_RESTAURANT_NAME)
    """
    method purpose: generating unique username of user, depending on their names
    future TODO: validate if names of employees duplicated, the username should be unique; maximum length of username
    """
    def __generate_username(self):
        names = self._name.lower().split()
        return '{}{}'.format(names[0][0], names[-1])

    """
    method purpose: implemented for manual and simple unit tests
    """
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
