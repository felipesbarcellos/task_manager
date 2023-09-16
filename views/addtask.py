from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class TaskLayout(BoxLayout):
    ...

class AddTaskApp(App):
    def build(self):
        return TaskLayout()
    ...

if __name__ == "__main__":
    AddTaskApp().run()