from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class HorizBox(Widget):
    pass

class RootUI(Widget):
    pass

class LabelFormat(Widget):
    pass

class rootuiApp(App):
    def build(self):
        self.balance = 2000
        return RootUI()