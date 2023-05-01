from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text='Hello Word', 
                        halign='center', 
                        theme_text_color='Custom', 
                        text_color=(0,0,0,1), 
                        font_style='H3')
        icon_label = MDIcon(icon='language-python',
                            halign='center')
        return label



DemoApp().run()