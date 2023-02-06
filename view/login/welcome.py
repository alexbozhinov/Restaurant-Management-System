"""
filename: welcome.py
author: alexbozhinov
created: 05.02.2023
purpose: definition of class WelcomeWindow - the first screen of the app
"""

from kivy.uix.widget import Widget
from kivy.lang import Builder

import constants

Builder.load_file('view/login/welcome.kv')


class WelcomeWindow(Widget):
    images_store = constants.IMAGES_SOURCE

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    """
    method purpose: on_click of button START RMS move to login screen
    """
    def welcome(self):
        self.parent.parent.current = 'screen_login'
