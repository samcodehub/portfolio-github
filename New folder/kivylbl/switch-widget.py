# import kivy module
import kivy

# base class of your application inherites from app class always refers to the instance of your app
from kivy.app import App

# below this kivy version you cannot use the app
kivy.require('1.9.0')

# the switch widget is active or inactive the state transition of a switch is from either on to off or off to on
from kivy.uix.switch import Switch

# the gridlayout arranges children in a matrix , it takes the available space and divides it into colums and rows
from kivy.uix.gridlayout import GridLayout

# the label widget is for rendering text
from kivy.uix.label import Label

# the config module is used to set the window size
from kivy.config import Config
Config.set('graphics','width','400')
Config.set('graphics','height','400')

# set the window background color
from kivy.core.window import Window
Window.clearcolor = (0.1, 0, 1, 1)

# a gridlayout with label a switch and a class which contains all stuff about switch
class SimpleSwitch(GridLayout):
    
    # defining __init__ constructor
    def __init__(self,**kwargs):
        
        # super function can be used to gain access to inherited methods from a parent or sibling class that has been overwitten in a class object
        super(SimpleSwitch, self).__init__(**kwargs)
        
        # number of columns
        self.cols = 2
        
        # adding label to the switch
        self.add_widget(Label(text = "Switch", font_size = 30))
        
        # initially switch is on active = true
        self.settings_sample = Switch(active = True)
        
        # add widget
        self.add_widget(self.settings_sample)
        
        # arranging a callback to switch using bind function
        self.settings_sample.bind(active = switch_callback)
        
# callback for the switch state transition, defining a callback function, contains two parameter switchobject, switchvalue
def switch_callback(switchObject, switchValue):
    
    # switch value are true and false
    if(switchValue):
        print("Switch is ON")
    else:
        print("Switch is OFF")
        
# defining the app class
class SwitchApp(App):
    # define build function
    def build(self):
        #return the switch class
        return SimpleSwitch()
    
# run the kivy app
if __name__=='__main__':
    SwitchApp().run()