# base class of your app
from kivy.app import App

# floatlayout allows us to place the elements relatively based on the current window size
from kivy.uix.floatlayout import FloatLayout

# box layout arranges children in a vertical or horizontal box
from kivy.uix.boxlayout import BoxLayout

# the kivy language is a language dedicated to describing user interface and interactions
from kivy.lang import Builder

# to change the kivy default setting we use config
from kivy.config import Config
Config.set('graphics','width','500')
Config.set('graphics','height','500')

# set the window background color
from kivy.core.window import Window
Window.clearcolor = (.3, .2, 0.7, 1)

Builder.load_string('''
<RootWidget>
    CustomLayout:
        AsyncImage:
            source: 'image/pic 3.png'
            size_hint: 1, 1
            pos_hint: {'center_x':.6, 'center_y': .8}
    AsyncImage:
        source: 'image/pic 2.png'
        size_hint: 1, 1
    CustomLayout
        AsyncImage:
            source: 'image/pic 1.png'
            size_hint: 1, 1
            pos_hint: {'center_x':.4, 'center_y': 0.2}
''')

class RootWidget(BoxLayout):
    pass

class CustomLayout(FloatLayout):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()