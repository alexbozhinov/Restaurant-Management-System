"""
filename: manager_main_screen.py
author: alexbozhinov
created: 13.02.2023
purpose: definition of class ManagerMainWindow - the main screen of employee type manager
"""

from kivy.lang import Builder
from kivy.uix.widget import Widget
from view.other_screens.profile_screen import ProfileWindow


# Builder.load_file('view/other_screens/profile_screen.kv')
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
        self.logged_manager = None
        self.parent.parent.current = 'screen_welcome'

    def manager_entered(self):
        # load image also

        self.ids.manager_name_label.text += self.controller.get_logged_manager().get_name()
        self.logged_manager = self.controller.get_logged_manager()

        self.children[0].children[0].children[0].children[0].logged_employee = self.logged_manager

        self.children[0].children[0].children[0].children[0].children[0].children[1].children[3].text +=\
            '{}'.format(self.logged_manager.get_name())
        self.children[0].children[0].children[0].children[0].children[0].children[1].children[2].text +=\
            'Manager'
        self.children[0].children[0].children[0].children[0].children[0].children[1].children[1].text +=\
            '{}'.format(self.logged_manager.get_username())
        self.children[0].children[0].children[0].children[0].children[0].children[1].children[0].text +=\
            '{}'.format(self.logged_manager.get_email())
