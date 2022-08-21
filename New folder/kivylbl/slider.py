# import kivy module
import kivy

# below this kivy version you cannot use the app
kivy.require("1.9.1")

# base class of your application inherites from app class always refers to the instance of your app
from kivy.app import App

# the gridlayout arranges children in a matrix
from kivy.uix.gridlayout import GridLayout

# importing slider widget
from kivy.uix.slider import Slider

# the label widget is for rendernig text
from kivy.uix.label import Label

# property that represents a numeric value between min, max
from kivy.properties import NumericProperty

# the config module is used to set the window size
from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')

# set the window background
from kivy.core.window import Window
Window.clearcolor = (0, 0, 1, 1)

# defining the slider and its effects class
class WidgetContainer(GridLayout):
    
    def __init__(self, **kwargs):
        
        # super function can be used to gain access to inherited methodes from a parent or sibling class that has been overwritten in class object
        super(WidgetContainer, self).__init__(**kwargs)
        
        # 4colums in grid
        self.cols = 4
        
        # declaring the slider and adding some effects to it , by default its orientation is horizontal. if you want to change it to vertical do it like below
        self.brightnessControl = Slider(min = 0, max = 100, orientation = 'vertical', value_track = True, value_track_color = [0, 1, 0, 1])
        
        # first row  one label, one slider
        self.add_widget(Label(text = 'brightness', font_size = 20))
        self.add_widget(self.brightnessControl)
        
        # second row one label for caption
        # one label for slider
        
        self.add_widget(Label(text = 'Slider Value', font_size = 20))
        self.brightnessValue = Label(text = '0', font_size = 20)
        self.add_widget(self.brightnessValue)
        # on the slider object attach a callback for the attribute named value
        self.brightnessControl.bind(value = self.on_value)
    
    # adding functionality behind the slider when pressed increase the value
    def on_value(self, instance, brightness):
        self.brightnessValue.text = "% d"% brightness

# the app class
class SliderExample(App):
    def build(self):
        widgetContainer = WidgetContainer()
        return widgetContainer
    
# creating the object root for buttonapp() class
root = SliderExample()

# run function runs the whole program
root.run()
