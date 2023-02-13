"""
filename: app.py
author: alexbozhinov
created: 05.02.2023
purpose: initializing the main window, initializing the app, initializing the database
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import constants
from database.db import DB
from view.login.login import LoginWindow
from view.login.welcome import WelcomeWindow
from view.main_employees_screens.chef_main_screen import ChefMainWindow
from view.main_employees_screens.manager_main_screen import ManagerMainWindow
from view.main_employees_screens.waiter_main_screen import WaiterMainWindow

Builder.load_file('app.kv')

# database initializing
db = DB()
db.create_database()

"""
The main window of the app, managed by kivy ScreenManager
"""


class MainWindow(BoxLayout):
    welcome_screen = WelcomeWindow()
    login_screen = LoginWindow()
    chef_main_screen = ChefMainWindow()
    waiter_main_screen = WaiterMainWindow()
    manager_main_screen = ManagerMainWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.screen_welcome.add_widget(self.welcome_screen)
        self.ids.screen_login.add_widget(self.login_screen)
        self.ids.screen_chef_main.add_widget(self.chef_main_screen)
        self.ids.screen_waiter_main.add_widget(self.waiter_main_screen)
        self.ids.screen_manager_main.add_widget(self.manager_main_screen)


"""
The app main class
"""


class RMS(App):
    images_store = constants.IMAGES_SOURCE

    def build(self):
        self.icon = constants.IMAGES_SOURCE + 'RMS_logo.png'
        Window.clearcolor = (240 / 255.0, 230 / 255.0, 170 / 255.0, 1)
        return MainWindow()


# start point of the app
if __name__ == "__main__":
    RMS().run()
