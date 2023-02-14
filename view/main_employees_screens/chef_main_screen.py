"""
filename: chef_main_screen.py
author: alexbozhinov
created: 13.02.2023
purpose: definition of class ChefMainWindow - the main screen of employee type chef
"""

from kivy.lang import Builder
from kivy.uix.widget import Widget
from view.other_screens.profile_screen import ProfileWindow


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
        self.logged_chef = None
        self.parent.parent.current = 'screen_welcome'

    def chef_entered(self):
        # add image also
        self.ids.chef_name_label.text += self.controller.get_logged_chef().get_name()
        self.logged_chef = self.controller.get_logged_chef()

        self.children[0].children[0].children[0].children[0].logged_employee = self.logged_chef

        self.children[0].children[0].children[0].children[0].children[0].children[1].children[3].text +=\
            '{}'.format(self.logged_chef.get_name())
        self.children[0].children[0].children[0].children[0].children[0].children[1].children[2].text +=\
            'Chef'
        self.children[0].children[0].children[0].children[0].children[0].children[1].children[1].text +=\
            '{}'.format(self.logged_chef.get_username())
        self.children[0].children[0].children[0].children[0].children[0].children[1].children[0].text +=\
            '{}'.format(self.logged_chef.get_email())
