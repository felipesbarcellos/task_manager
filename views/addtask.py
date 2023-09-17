from utils.constants import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex(WINDOW_COLOR)

class TaskLayout(BoxLayout):
    ...

class AddTaskApp(App):
    def build(self):
        return TaskLayout()
    ...

if __name__ == "__main__":
    AddTaskApp().run()