# import kivy module
import kivy

# base class of your application inherites from app class always refers to the instance of your app
from kivy.app import App

# below this kivy version you can not use the app
kivy.require('1.9.0')

# the progressbar widget is used to visualize the progress of some task
from kivy.uix.progressbar import ProgressBar

# box layout arranges children in a vertical or horizontal box
from kivy.uix.boxlayout import BoxLayout

# the clock object allows you to schedule a function call in future
from kivy.clock import Clock

# the button is a label with associated actions that is triggered when the button is pressed
from kivy.uix.button import Button

# popup widget is used to create popups, by default the popup will cover the whole parent window, when you are creating a popup you must at least set a popup title and popup content
from kivy.uix.popup import Popup

# a widget is the base building block of gui interfaces in kivy, it provides a canvas that can be used to draw on screen
from kivy.uix.widget import Widget

# objectproperty is a specialized subclass of the property class, so it has same initialization parameters as it . by default a property always takes a default value. the default value must be a value that agrees wih the property
from kivy.properties import ObjectProperty

# the config module is used to set the window size
from kivy.config import Config
Config.set('graphics','width','500')
Config.set('graphics','height','400')

# set the window background color
from kivy.core.window import Window
Window.clearcolor = (0.1, 0.5, 0.1, 1)

# create the widget class
class MyWidget(Widget):
    progress_bar = ObjectProperty()
    
    def __init__(self, **kwa):
        super(MyWidget, self).__init__(**kwa)
        
        self.progress_bar = ProgressBar()
        self.popup = Popup(title = 'Download', content = self.progress_bar)
        
        self.popup.bind(on_open = self.puopen)
        self.add_widget(Button(size = (200, 60), pos = (150, 150), text = 'Download', font_size = 30, background_color = (0, 0.7, 1, 1), on_release = self.pop))
        
    # the function which works when you click the button
    def pop(self, instance):
        self.progress_bar.value = 1
        self.popup.open()
        
    # to continuosly increasing the alue of pb
    def next(self, dt):
        if self.progress_bar.value>= 100:
            return False
        self.progress_bar.value += 1
            
    # as the number increase the progress speed will increase
    def puopen(self, instance):
            Clock.schedule_interval(self.next, 1/3)
# create the app class
class ProgressApp(App):
    def build(self):
        return MyWidget()
# run the app
if __name__ in ("__main__"):
    ProgressApp().run()


#python kivy tutorial,
#python kivy projects,
#progress bar python,
#progress bar kivy,
#kivy loading screen,
#kivy clock,
#kivy clock schedule_once,
#kivy vs tkinter,
#kivy button, 
#kivy button position,
#kivy button pos_hint,
#kivy popup example,
#python kivy gui,
#python for beginners,
        