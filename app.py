from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import constants
from view.login.login import LoginWindow
from view.login.welcome import WelcomeWindow
from kivy.uix.screenmanager import ScreenManager, NoTransition

Builder.load_file('app.kv')


class MainWindow(BoxLayout):
    welcome_screen = WelcomeWindow()
    login_screen = LoginWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.screen_welcome.add_widget(self.welcome_screen)
        self.ids.screen_login.add_widget(self.login_screen)


class RMS(App):
    images_store = constants.IMAGES_SOURCE

    def build(self):
        self.icon = constants.IMAGES_SOURCE + 'RMS_logo.png'
        Window.clearcolor = (240/255.0, 230/255.0, 170/255.0, 1)
        return MainWindow()


if __name__ == "__main__":
    RMS().run()
