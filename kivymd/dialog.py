from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
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
    
    def show_date(self, mld):
        if self.username.text is "":
            check_string = 'Entrer un nom svp !'
        else:
            check_string = self.username.text + " n'existe pas "
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog = MDDialog(text=check_string,
                          title='Votre Nom',
                          buttons=[close_button, more_button])
        self.dialog.open()

    def close_dialog(self, mld):
        self.dialog.dismiss()


DemoApp().run()