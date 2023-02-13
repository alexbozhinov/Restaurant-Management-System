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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    """
    method purpose: go back to the welcome window of the app 
    """
    def exit(self):
        self.parent.parent.current = 'screen_welcome'