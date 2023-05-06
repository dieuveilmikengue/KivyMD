from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from aide import username_helper


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        btn = MDRectangleFlatButton(text='Show',
                                    pos_hint={'center_x':0.5, 'center_y':0.4},
                                    on_release=self.show_date)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(btn)
        return screen
    
    def show_date(self, mio):
        print(self.username.text)


DemoApp().run()