# import module
import kivy

# base class of your app
from kivy.app import App

# creates the button in kivy
from kivy.uix.button import Button

# this layout allows you to set relative coordinates for children
from kivy.uix.relativelayout import RelativeLayout

# to change the kivy default setting we use config
from kivy.config import Config

Config.set('graphics','width','400')
Config.set('graphics','height','400')

# set the window background color
from kivy.core.window import Window
Window.clearcolor = (0.2, 0, .1, 1)

# creating the app class
class Relative_Layout(App):
    def build(self):
        
        # creating relativelayout
        rl = RelativeLayout()
        
        # creating button and positioning them on bottom-left, bottom-right, center,top-left and top-right
        # size of button is 10% by height and 20% width of your layout
        b1 = Button(size_hint = (.2, .1), pos_hint = {'x':0, 'y':0}, text = "B1", background_color = (0, 1, .5))
        
        b2 = Button(size_hint = (.2, .1), pos_hint ={'right':1 ,'y':0}, text = "B2", background_color = (0, 1, .5))
        
        b3 = Button(size_hint = (.2, .1), pos_hint = {'center_x':.5, 'center_y':.5}, text = "B3", background_color = (.1, 1, 1))
        
        b4 = Button(size_hint = (.2, .1), pos_hint ={'x':0, 'top':1}, text = "B4", background_color = (0, 1, .5))
        
        b5 = Button(size_hint = (.2, .1), pos_hint = {'right':1, 'top':1}, text = "B5", background_color = (0, 1, .5))
        
        # adding button to widget
        rl.add_widget(b1)
        rl.add_widget(b2)
        rl.add_widget(b3)
        rl.add_widget(b4)
        rl.add_widget(b5)
        
        # returnig widget
        return rl

# run the app
if __name__=="__main__":
    Relative_Layout().run()