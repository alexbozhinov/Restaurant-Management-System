from kivy.uix.widget import Widget
from kivy.lang import Builder

import constants

Builder.load_file('view/login/welcome.kv')


class WelcomeWindow(Widget):
    images_store = constants.IMAGES_SOURCE

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def welcome(self):
        self.parent.parent.current = 'screen_login'

