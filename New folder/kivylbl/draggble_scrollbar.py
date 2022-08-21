# import kivy module
import kivy

#below this kivy version you cannot use the app
kivy.require('1.5.1')

# to change the kivy default setting we use config
from kivy.config import Config
Config.set('graphics','width','500')
Config.set('graphics','height','500')

# base class of your app
from kivy.app import App

# creates the button in kivy
from kivy.uix.button import Button

# the stacklayout arranges children vertically and horizontally , as many as the layout can fit.
from kivy.uix.stacklayout import StackLayout

# the grid layout arranges children in a matrix, it takes the available space and divides it into columns and rows
from kivy.uix.gridlayout import GridLayout

# the textinput widget provides a box for editable plain text
from kivy.uix.textinput import TextInput

# popup widget is used to create popups. by defualt the popup will cover whole parent window. when you are creating popup you must at least set popup title and popup content
from kivy.uix.popup import Popup

# the scrollview manages the position of its children similrly to relaytivelayout but does not use the size_hint
from kivy.uix.scrollview import ScrollView

# importing slider widget
from kivy.uix.slider import Slider

# partial function allow one to derive a function with x parameters to a function with fewer parameters and fixed values set for the more limited function
from functools import partial

class ScrollApp(App):
    
    def build(self):
        popup = Popup(title='Draggable Scrollbar', size_hint=(0.8,1), auto_dismiss=False)

        #this layout is the child widget for the main popup
        layout1 = StackLayout(orientation='lr-bt')

        #this button is a child of layout1
        closebutton = Button(text='close', size_hint=(0.9,0.05))
        closebutton.bind(on_press=popup.dismiss)

        #another child of layout1 and this is the scrollview which will have a custom draggable scrollbar
        scrlv = ScrollView(size_hint=(0.9,0.95))

        #the last child of layout1 and this will act as the draggable scrollbar
        s = Slider(min=0, max=1, value=25, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))

        scrlv.bind(scroll_y=partial(self.slider_change, s))

        #what this does is, whenever the slider is dragged, it scrolls the previously added scrollview by the same amount the slider is dragged
        s.bind(value=partial(self.scroll_change, scrlv))

        layout2 = GridLayout(cols=3, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        for i in range(0, 99):
            btn = Button(text=str(i), size_hint_y=None, height=120, valign='center', font_size=20, background_color = (0,.8,.8,.8))
            btn.text_size = (btn.size)
            layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()

    def scroll_change(self, scrlv, instance, value):
        scrlv.scroll_y = value

    def slider_change(self, s, instance, value):
        if value >= 0:
        #this to avoid 'maximum recursion depth exceeded' error
            s.value=value

# run the app
if __name__ == '__main__':
    ScrollApp().run()
    

