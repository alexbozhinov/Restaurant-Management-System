"""
filename: manager_main_screen.py
author: alexbozhinov
created: 13.02.2023
purpose: definition of class ManagerMainWindow - the main screen of employee type manager
"""

from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('view/main_employees_screens/manager_main_screen.kv')


class ManagerMainWindow(Widget):
    def __init__(self, controller, **kwargs):
        self.controller = controller
        self.logged_manager = None
        super().__init__(**kwargs)

    """
    method purpose: go back to the welcome window of the app 
    """
    def exit(self):
        self.parent.parent.current = 'screen_welcome'

    def manager_entered(self):
        self.ids.manager_name_label.text = self.controller.get_logged_manager().get_name()
        self.logged_manager = self.controller.get_logged_manager()
