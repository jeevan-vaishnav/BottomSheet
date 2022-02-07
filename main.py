from ast import Lambda
import imp
from turtle import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
# from kivymd.uix.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory
import webbrowser
Window.size = (400, 600)


class Screen1(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Screen1(name="s1"))


class BottomSheet(MDApp):
    def build(self):
        screen = Screen()
        # Import KV MD File
        self.kv = Builder.load_file('main.kv')
        screen.add_widget(self.kv)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Lime"
        return screen

    def ShowBottomSheet(self):
        self.custom = MDCustomBottomSheet(screen=Factory.CustomSheet())
        self.custom.open()

    def open(self):
        webbrowser.open_new("www.google.com")

        #
        #
        #
        ##
        #
        #
        # Second
        # def callback_(self, *args):
        #     toast(args[0])
        # def buttom_layer(self):
        #     data = {
        #         "Facebook": 'facebook-box',
        #         "YouTube": 'youtube',
        #         "Instagram": 'instagram',
        #         "Twitter": 'twitter-box',
        #         "Camera": 'camera'
        #     }
        #     bottom_sheet = MDGridBottomSheet(radius=20, radius_from="top")
        #     for item in data.items():
        #         bottom_sheet.add_item(
        #             item[0],
        #             lambda x, y=item[0]: self.callback_(y),
        #             icon_src=item[1]
        #         )
        #     bottom_sheet.open()

        # First
        # def callback_(self, *args):
        #     toast(args[0])
        # def buttom_layer(self):
        #     bottom_sheet = MDListBottomSheet(radius=20, radius_from='top')
        #     for i in range(10):
        #         bottom_sheet.add_item(
        #             f"Item {i+1}",
        #             lambda x, y=i+1: self.callback_(f"Item {y} Clicked"),
        #             icon='android'
        #         )
        #     bottom_sheet.open()
if __name__ == "__main__":
    BottomSheet().run()
