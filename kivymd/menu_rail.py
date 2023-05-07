from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView

KV = '''
<ContentNavigationDrawer>

    MDList:

        OneLineListItem:
            Image:
                source: "mike.png"
                pos_hint: {'center_x':0.5, 'center_y':0.1}
                size_hint_y: None 


        OneLineListItem:
            text: "Screen 1"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"

        OneLineListItem:
            text: "Screen 2"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"

        OneLineListItem:
            text: "Screen 3"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 3"

            


MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        title: "CAP"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                Image:
                    source: "mike.png"

                MDLabel:
                    text: "Je m'appel Mikengue lebake dieuveil diska j'enseigne python et mes domaines de competences sont  Developpement mobile  Machine learning Developpement Web"
                    halign: "justify"
                    padding: "10dp"

            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    padding: "10dp"

            MDScreen:
                name: "scr 3"

                MDLabel:
                    text: "Screen 3"
                    halign: "center"
                    padding: "10dp"

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 10, 10, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Menu_rail(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Menu_rail().run()