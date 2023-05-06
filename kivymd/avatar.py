from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineIconListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivy.uix.scrollview import ScrollView


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()

        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range(20):
            image = ImageLeftWidget(source="youtube.png")
            items = ThreeLineIconListItem(text='Item ' +  str(i),
                                      secondary_text='Deuxieme texte',
                                      tertiary_text='Troisieme texte')
            items.add_widget(image)
            list_view.add_widget(items)

        

        screen.add_widget(scroll)

        return screen


DemoApp().run()