from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button


class ProfileWindow(Widget):
    def __init__(self, **kwargs):
        self.logged_employee = None
        self.salary_showed = False
        self.change_password_showed = False

        self.empty_label_1 = Label(text='')
        self.current_password_label = Label(
            text='Current password: ',
            font_size=20,
            color=(137/255.0, 96/255.0, 0/255.0, 1)
        )
        self.current_password_input = TextInput(
            hint_text=' Input here',
            font_size=20,
            multiline=False,
            background_normal='',
            foreground_color=(137 / 255.0, 96 / 255.0, 0 / 255.0, 1),
            hint_text_color=(148 / 255.0, 129 / 255.0, 84 / 255.0, 1),
            background_color=(243/255.0, 227/255.0, 172/255.0, 1),
            focus=False
        )
        self.new_password_label = Label(
            text='New password:       ',
            font_size=20,
            color=(137 / 255.0, 96 / 255.0, 0 / 255.0, 1)
        )
        self.new_password_input = TextInput(
            hint_text='Input here',
            font_size=20,
            multiline=False,
            background_normal='',
            foreground_color=(137 / 255.0, 96 / 255.0, 0 / 255.0, 1),
            hint_text_color=(148 / 255.0, 129 / 255.0, 84 / 255.0, 1),
            background_color=(243 / 255.0, 227 / 255.0, 172 / 255.0, 1),
            focus=False
        )
        self.save_changes_button = Button(
            text='Save Changes',
            background_normal='',
            background_color=(255 / 255.0, 205 / 255.0, 0 / 255.0, 1)
        )
        super().__init__(**kwargs)

    def salary_button_press(self):
        self.set_logged_employee()
        if not self.salary_showed:
            self.salary_showed = True
            self.ids.salary_label.text = str(self.logged_employee.get_salary().get_money())
        else:
            self.salary_showed = False
            self.ids.salary_label.text = ''

    def change_password_button_clicked(self):
        self.set_logged_employee()
        if not self.change_password_showed:
            self.change_password_showed = True
            self.ids.salary_password_layout.remove_widget(self.ids.empty_label_2)
            self.ids.salary_password_layout.remove_widget(self.ids.empty_label_3)
            self.ids.salary_password_layout.remove_widget(self.ids.empty_label_4)
            self.ids.salary_password_layout.remove_widget(self.ids.empty_label_5)
            self.ids.salary_password_layout.remove_widget(self.ids.empty_label_6)
            self.ids.salary_password_layout.remove_widget(self.ids.empty_label_7)
            self.ids.salary_password_layout.remove_widget(self.ids.empty_label_8)

            self.ids.salary_password_layout.add_widget(self.current_password_label)
            self.ids.salary_password_layout.add_widget(self.current_password_input)
            self.ids.salary_password_layout.add_widget(self.new_password_label)
            self.ids.salary_password_layout.add_widget(self.new_password_input)

            self.ids.salary_password_layout.add_widget(self.ids.empty_label_2)
            self.ids.salary_password_layout.add_widget(self.ids.empty_label_3)
            self.ids.salary_password_layout.add_widget(self.save_changes_button)
            self.ids.salary_password_layout.add_widget(self.ids.empty_label_4)
            self.ids.salary_password_layout.add_widget(self.ids.empty_label_5)
            self.ids.salary_password_layout.add_widget(self.ids.empty_label_6)
            self.ids.salary_password_layout.add_widget(self.ids.empty_label_7)
            self.ids.salary_password_layout.add_widget(self.ids.empty_label_8)
        else:
            self.change_password_showed = False
            self.ids.salary_password_layout.remove_widget(self.current_password_label)
            self.ids.salary_password_layout.remove_widget(self.current_password_input)
            self.ids.salary_password_layout.remove_widget(self.new_password_label)
            self.ids.salary_password_layout.remove_widget(self.new_password_input)
            self.ids.salary_password_layout.remove_widget(self.save_changes_button)

    def set_logged_employee(self):
        if hasattr(self.parent.parent.parent.parent, 'logged_manager'):
            self.logged_employee = self.parent.parent.parent.parent.logged_manager
        elif hasattr(self.parent.parent.parent.parent, 'logged_chef'):
            self.logged_employee = self.parent.parent.parent.parent.logged_chef
        elif hasattr(self.parent.parent.parent.parent, 'logged_waiter'):
            self.logged_employee = self.parent.parent.parent.parent.logged_waiter
