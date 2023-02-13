"""
filename: chef_main_screen.py
author: alexbozhinov
created: 13.02.2023
purpose: definition of class ChefMainWindow - the main screen of employee type chef
"""

from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('view/main_employees_screens/chef_main_screen.kv')


class ChefMainWindow(Widget):
    def __init__(self, controller,  **kwargs):
        self.controller = controller
        self.logged_chef = None
        super().__init__(**kwargs)

    """
    method purpose: go back to the welcome window of the app 
    """
    def exit(self):
        self.parent.parent.current = 'screen_welcome'

    def chef_entered(self):
        self.ids.chef_name_label.text = self.controller.get_logged_chef().get_name()
        self.logged_chef = self.controller.get_logged_chef()
