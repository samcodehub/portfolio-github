# import kivy module
import kivy

# mdscreen is an element intended to be used with a screenmanager
from kivymd.uix.screen import MDScreen

# mdapp class that is inherited from app
from kivymd.app import MDApp

# importing mdfloatingactionbuttonspeeddial to use it in the app
from kivymd.uix.button import MDFloatingActionButtonSpeedDial

# core class for creating the default kivy window and size the window
from kivy.core.window import Window
Window.size = (500, 500)

# create the app class
class Example(MDApp):
    # adding icons and items
    data = {
        'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp',
    }
    def build(self):
        self.theme_cls.theme_style = "Dark" # or "Light" ,"normal","darkest"
        screen = MDScreen()
        speed_dial = MDFloatingActionButtonSpeedDial()
        speed_dial.data = self.data
        speed_dial.root_button_anim = True
        screen.add_widget(speed_dial)
        return screen
Example().run()