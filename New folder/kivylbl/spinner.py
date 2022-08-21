# import kivy module
import kivy

# base class of your app
from kivy.app import App

# below this kivy version you cannot use the app
kivy.require('1.9.0')

# to change the kivy default setting we use config
from kivy.config import Config
Config.set('graphics','width','500')
Config.set('graphics','height','500')

# the label widget is for rendering text
from kivy.uix.label import Label

# spinner is a widget that provides a quick way to select one value from a set like a dropdown list
from kivy.uix.spinner import Spinner

# floatlayout allows us to place the elements relatively based on the current window size and height
from kivy.uix.floatlayout import FloatLayout

# make an app by deriving from the app class
class SpinnerExample(App):
    # defIne build
    def build(self):
        
        # creating floatlayout
        layout = FloatLayout()
        
        # creating the spinner , configure spinner object and add to layout
        self.SpinnerObject = Spinner(text = "Languages List",
                                     values = ("Python","Java","C++", "C","C#","PHP"), background_color = (0.84, 0.3, 0.6, 1))
        
        self.SpinnerObject.size_hint = (0.3, 0.1)
        
        self.SpinnerObject.pos_hint = {'x': .10, 'y': .75}
        
        layout.add_widget(self.SpinnerObject)
        
        self.SpinnerObject.bind(text = self.on_spinner_select)
        
        # it change the label info as well add a label displaying the selection from the spinner
        self.SpinnerSelection = Label(text = "Selected item is: %s"%self.SpinnerObject.text)
        
        layout.add_widget(self.SpinnerSelection)
        self.SpinnerSelection.pos_hint = {'x': .175, 'y': .3}
        
        return layout
    
    # call back for the selection in spinner object
    def on_spinner_select(self, spinner, text):
        self.SpinnerSelection.text = "Your language is: %s"%self.SpinnerObject.text
        print('The spinner', spinner, 'have text', text)
        
# run the app
if __name__=='__main__':
    SpinnerExample().run()
        
                
        