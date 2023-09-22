from utils.constants import *
from kivy.app import App
from components import components

class MenuApp(App):
    def build(self):
        return components.Menu()

if __name__ == "__main__":
    MenuApp().run()