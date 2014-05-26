from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout

class TestApp(App):
    def build(self):
        l = Label(text='Hola!!',  font_size=160)
        f = FloatLayout()
        s = Scatter()

        f.add_widget(s)
        s.add_widget(l)
        return f
TestApp().run()
