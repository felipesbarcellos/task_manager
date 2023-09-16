from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex("#05050c")

class Menu(BoxLayout):
    ...

class MenuApp(App):
    def build(self):
        return Menu()

if __name__ == "__main__":
    MenuApp().run()