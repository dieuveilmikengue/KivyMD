from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Orange"
        self.theme_cls.primary_hue="A400"
        self.theme_cls.theme_style="Dark"
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Hello Word',
                                         pos_hint={'center_x':0.5, 'center_y':0.5})
        icon_button = MDIconButton(icon='android',
                                   pos_hint={'center_x':0.5, 'center_y':0.5})
        screen.add_widget(btn_flat)
        return screen



DemoApp().run()