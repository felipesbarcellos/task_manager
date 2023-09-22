from utils.constants import *
from kivy.app import App
from components import components

class AddTaskApp(App):
    def build(self):
        return components.TaskLayout()
    ...

if __name__ == "__main__":
    AddTaskApp().run()