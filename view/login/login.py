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
from controller.employees.managers_controller import ManagersController
from controller.employees.waiters_controller import WaitersController

Builder.load_file('view/login/login.kv')


class LoginWindow(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__employee_type = ''
        self.chefs_controller = ChefsController()
        self.waiters_controller = WaitersController()
        self.managers_controller = ManagersController()

    def employee_type_spinner_clicked(self, value):
        self.__employee_type = value
    """
    method purpose: apply login via sending the inputted email and password to the controller for validation 
    """
    def __apply_chef_login(self):
        email = self.ids.email_input.text
        password = self.ids.password_input.text

        # if textinput is not filled
        if email == '' or password == '':
            self.unfilled_data_popup()
        else:
            # if the inputted email and password exist in the database's table chefs
            if self.chefs_controller.check_login(email, password):
                self.chef_successful_login()
            else:
                self.chef_fail_login()
    """
    method purpose: apply login via sending the inputted email and password to the controller for validation 
    """
    def __apply_waiter_login(self):
        email = self.ids.email_input.text
        password = self.ids.password_input.text

        # if textinput is not filled
        if email == '' or password == '':
            self.unfilled_data_popup()
        else:
            # if the inputted email and password exist in the database's table waiters
            if self.waiters_controller.check_login(email, password):
                self.waiter_successful_login()
            else:
                self.waiter_fail_login()

    """
    method purpose: apply login via sending the inputted email and password to the controller for validation 
    """
    def __apply_manager_login(self):
        email = self.ids.email_input.text
        password = self.ids.password_input.text

        # if textinput is not filled
        if email == '' or password == '':
            self.unfilled_data_popup()
        else:
            # if the inputted email and password exist in the database's table managers
            if self.managers_controller.check_login(email, password):
                self.manager_successful_login()
            else:
                self.manager_fail_login()

    """
    method purpose: on successful chef login, move to next screen
    """
    def chef_successful_login(self):
        print("Chef successful login")
        self.ids.email_input.text = ''
        self.ids.password_input.text = ''
        self.ids.employee_type_spinner.text = 'Select Position'

        self.parent.parent.current = 'screen_chef_main'

    """
    method purpose: on unsuccessful chef login, show popup saying there is an error
    """
    def chef_fail_login(self):
        self.incorrect_data_popup()

        # clear the text inputs
        self.ids.email_input.text = ''
        self.ids.password_input.text = ''
        self.ids.employee_type_spinner.text = 'Select Position'

    """
    method purpose: on successful waiter login, move to next screen
    """
    def waiter_successful_login(self):
        print("Waiter successful login")
        self.ids.email_input.text = ''
        self.ids.password_input.text = ''
        self.ids.employee_type_spinner.text = 'Select Position'

        self.parent.parent.current = 'screen_waiter_main'

    """
    method purpose: on unsuccessful waiter login, show popup saying there is an error
    """
    def waiter_fail_login(self):
        self.incorrect_data_popup()

        # clear the text inputs
        self.ids.email_input.text = ''
        self.ids.password_input.text = ''
        self.ids.employee_type_spinner.text = 'Select Position'

    """
    method purpose: on successful manager login, move to next screen
    """
    def manager_successful_login(self):
        print("Manager successful login")
        self.ids.email_input.text = ''
        self.ids.password_input.text = ''
        self.ids.employee_type_spinner.text = 'Select Position'

        self.parent.parent.current = 'screen_manager_main'

    """
    method purpose: on unsuccessful manager login, show popup saying there is an error
    """
    def manager_fail_login(self):
        self.incorrect_data_popup()

        # clear the text inputs
        self.ids.email_input.text = ''
        self.ids.password_input.text = ''
        self.ids.employee_type_spinner.text = 'Select Position'

    """
    method purpose: event on button LOGIN click
    """
    def login_click(self):
        if self.__employee_type == 'Manager':
            self.__apply_manager_login()
        elif self.__employee_type == 'Chef':
            self.__apply_chef_login()
        elif self.__employee_type == 'Waiter':
            self.__apply_waiter_login()
        else:
            self.unselected_employee_type_popup()

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

    """
    method purpose: creating and showing popup window with error message when spinner employee type not selected
    """
    @staticmethod
    def unselected_employee_type_popup():
        popup = Popup(
            title='Login Error',
            content=Label(text='Select Position field required!',
                          font_size=20,
                          color=(1, 0, 0, 1)),
            size_hint=(None, None),
            size=(300, 300),
            separator_color=(255 / 255.0, 128 / 255.0, 0 / 255.0, 1)
        )
        popup.open()
