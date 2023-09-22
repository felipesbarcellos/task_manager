from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from utils.constants import *
from kivy.lang import Builder
Window.clearcolor = WINDOW_COLOR

try:
    Builder.load_file('components.kv')
except:
    Builder.load_file('components/components.kv')
    pass

class Campo(BoxLayout):
    ...

class SmoothButton(Button):
    ...

class Menu(BoxLayout):
    ...

class TaskLayout(BoxLayout):
    ...

if __name__ == "__main__":
    from kivy.app import App

    class TestApp(App):
        def build(self):
            return Menu()
    
    TestApp().run()