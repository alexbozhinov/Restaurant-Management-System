"""
filename: login.py
author: alexbozhinov
created: 05.02.2023
purpose: definition of class LoginWindow - the login screen of the app
"""

from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.label import Label

from controller.employees.chefs_controller import ChefsController

Builder.load_file('view/login/login.kv')


class LoginWindow(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = ChefsController()

    def employee_type_spinner_clicked(self, value):
        print(value)
    """
    method purpose: apply login via sending the inputted email and password to the controller for validation 
    """
    def __apply_login(self):
        email = self.ids.email_input.text
        password = self.ids.password_input.text

        # if textinput is not filled
        if email == '' or password == '':
            self.unfilled_data_popup()
        else:
            # if the inputted email and password exist in the database's table chefs
            if self.controller.check_login(email, password):
                self.chef_successful_login()
            else:
                self.chef_fail_login()

    """
    method purpose: on successful login, move to next screen
    """
    def chef_successful_login(self):
        print("Chef successful login")
        # next screen

    """
    method purpose: on unsuccessful login, show popup saying there is an error
    """
    def chef_fail_login(self):
        self.incorrect_data_popup()

        # clear the text inputs
        self.ids.email_input.text = ''
        self.ids.password_input.text = ''

    """
    method purpose: event on button LOGIN click
    """
    def login_click(self):
        self.__apply_login()

    """
    method purpose: creating and showing popup window with error message when an input was not filled
    """
    @staticmethod
    def unfilled_data_popup():
        popup = Popup(
            title='Login Error',
            content=Label(text='Both email and password \nfields are required!',
                          font_size=20,
                          color=(1, 0, 0, 1)),
            size_hint=(None, None),
            size=(300, 300),
            separator_color=(255 / 255.0, 128 / 255.0, 0 / 255.0, 1)
        )
        popup.open()

    """
    method purpose: creating and showing popup window with error message when email or password are incorrect
    """
    @staticmethod
    def incorrect_data_popup():
        popup = Popup(
            title='Login Error',
            content=Label(text='Incorrect email or password',
                          font_size=20,
                          color=(1, 0, 0, 1)),
            size_hint=(None, None),
            size=(300, 300),
            separator_color=(255 / 255.0, 128 / 255.0, 0 / 255.0, 1)
        )
        popup.open()
