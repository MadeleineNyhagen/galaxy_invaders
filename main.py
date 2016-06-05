from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from player import Player

Builder.load_file('sprites.kv')

class Fleet(GridLayout):
    pass

class GalaxyInvaders(FloatLayout):
    pass

class GalaxyInvadersApp(App):
    def build(self):
        return GalaxyInvaders()

if __name__ == '__main__':
    GalaxyInvadersApp().run()