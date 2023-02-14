"""
filename: waiter_main_screen.py
author: alexbozhinov
created: 13.02.2023
purpose: definition of class WaiterMainWindow - the main screen of employee type waiter
"""

from kivy.lang import Builder
from kivy.uix.widget import Widget
from view.other_screens.profile_screen import ProfileWindow


Builder.load_file('view/main_employees_screens/waiter_main_screen.kv')


class WaiterMainWindow(Widget):
    def __init__(self, controller,  **kwargs):
        self.controller = controller
        self.logged_waiter = None
        super().__init__(**kwargs)

    def set_logged_waiter(self, waiter):
        self.logged_waiter = waiter

    """
    method purpose: go back to the welcome window of the app 
    """
    def exit(self):
        self.logged_waiter = None
        self.parent.parent.current = 'screen_welcome'

    def waiter_entered(self):
        self.ids.waiter_name_label.text += self.controller.get_logged_waiter().get_name()
        self.logged_waiter = self.controller.get_logged_waiter()

        self.children[0].children[0].children[0].children[0].logged_employee = self.logged_waiter

        self.children[0].children[0].children[0].children[0].children[0].children[1].children[3].text +=\
            '{}'.format(self.logged_waiter.get_name())
        self.children[0].children[0].children[0].children[0].children[0].children[1].children[2].text +=\
            'Waiter'
        self.children[0].children[0].children[0].children[0].children[0].children[1].children[1].text +=\
            '{}'.format(self.logged_waiter.get_username())
        self.children[0].children[0].children[0].children[0].children[0].children[1].children[0].text +=\
            '{}'.format(self.logged_waiter.get_email())
