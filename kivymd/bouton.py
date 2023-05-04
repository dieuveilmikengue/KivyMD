from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton, MDFloatingActionButton, MDRectangleFlatButton, MDRaisedButton, MDRectangleFlatIconButton


class DemoApp(MDApp):
    def build(self):
        box = MDBoxLayout(
            orientation='vertical',
            spacing=15,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
                      
        btn1 = MDFlatButton(
            text='login',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        btn2 = MDIconButton(
            icon='home',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        btn3 = MDFloatingActionButton(
            icon='plus',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        btn4 = MDRectangleFlatButton(
            text='Bouton',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        btn5 = MDRaisedButton(
            text='Bouton',
            icon='home',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        btn6 = MDRectangleFlatIconButton(
            text='Bouton',
            icon='home',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        box.add_widget(btn2)
        box.add_widget(btn1)
        box.add_widget(btn3)
        box.add_widget(btn4)
        box.add_widget(btn5)
        box.add_widget(btn6)

        return box



DemoApp().run()