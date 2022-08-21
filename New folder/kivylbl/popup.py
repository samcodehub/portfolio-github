# import kivy module
import kivy

# base class of your application inherites from app class always refers to the instance of your app
from kivy.app import App

# below this kivy version you cannot use the app
kivy.require('1.9.0')

# creating the button in kivy if not imported shows error
from kivy.uix.button import Button

# the grid layout arranges children in a matrix .it takes the available space and divides it into colums and rows
from kivy.uix.gridlayout import GridLayout

# popup widget is used to create popups. by default the popup will cover the whole parent window. when you are creating popup you must at least set popup title and popup content
from kivy.uix.popup import Popup

# the label widget is for rendering text
from kivy.uix.label import Label

# the config module is used to set the window size
from kivy.config import Config
Config.set('graphics','width','500')
Config.set('graphics','height','500')

# set the window background color
from kivy.core.window import Window
Window.clearcolor = (0.1, 0, 1, 1)

# make an app by deriving from the kivy provided app class
class PopupExample(App):
    # override the build method and return the root widget of this app
    def build(self):
        # define a grid layout for this app
        self.layout = GridLayout(cols = 1, padding = 150)
        
        # add a button
        self.button = Button(text ="Click for popup", font_size = 20, background_color=[0,1,0,1])
        self.layout.add_widget(self.button)
        
        # attach a callback for the button press event
        self.button.bind(on_press = self.onButtonPress)
        
        return self.layout
    # on button press create a popup dialog with label and a close button
    def onButtonPress(self, button):
        layout = GridLayout(cols = 1, padding = 10)
    
        popupLabel = Label(text = "This is a Pop-up")
        closeButton = Button(text = "Close The Pop-up", background_color = [1,0,0,1])
    
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)
    
        # instantiate the popup and display
        popup = Popup(title = 'Notification Popup!', content = layout, size_hint =(None, None),size =(200, 200))
    
        popup.open()
    
        # attach close button press with pop.dismiss action
        closeButton.bind(on_press = popup.dismiss)
    
# run the app
if __name__ =='__main__':
    PopupExample().run()