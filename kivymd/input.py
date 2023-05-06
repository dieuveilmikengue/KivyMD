from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder


username_helper = """

MDTextField:
    hint_text: "Etrer un nom"
    helper_text: "Message d'aide en dessous de l'input"
    helper_text_mode: "persistent"
    icon_right: "android"
    pos_hint: {'center_x':0.5, 'center_y':0.5}
    size_hint_x: None
    width: 300
"""

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        # username = MDTextField(text='Entrer votre nom',
        #                     pos_hint={'center_x':0.5, 'center_y':0.5},
        #                     size_hint_x=None,
        #                     width=300
        #                     )
        username = Builder.load_string(username_helper)
        screen.add_widget(username)
        return screen


DemoApp().run()