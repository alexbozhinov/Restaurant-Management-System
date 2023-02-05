from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.label import Label


Builder.load_file('view/login/login.kv')


class LoginWindow(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def unfilled_data_popup():
        popup = Popup(
            title='Login Error',
            content=Label(text='Both email and password \nfields are required!',
                          font_size=20,
                          color=(1, 0, 0, 1)),
            size_hint=(None, None),
            size=(300, 300),
            separator_color=(255/255.0, 128/255.0, 0/255.0, 1)
        )
        popup.open()

    @staticmethod
    def incorrect_data_popup():
        popup = Popup(
            title='Login Error',
            content=Label(text='Incorrect email or password',
                          font_size=20,
                          color=(1, 0, 0, 1)),
            size_hint=(None, None),
            size=(300, 300),
            separator_color=(255/255.0, 128/255.0, 0/255.0, 1)
        )
        popup.open()

    def validate_user(self):
        email = self.ids.email_input.text
        password = self.ids.password_input.text

        if email == '' or password == '':
            # popup window with error or label, here connection with controller and database
            # email regex validation, password decode, encode
            print('Email and Password fields required!')
            self.unfilled_data_popup()
        else:
            if email == 'admin' and password == 'admin':
                print('Logged successfully!')
            else:
                self.incorrect_data_popup()

