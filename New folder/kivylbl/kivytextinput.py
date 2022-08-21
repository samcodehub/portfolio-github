import kivy

# base class of your app inherite from app class always refers to the instance of your application
from kivy.app import App

# below this kivy version you can not use the app
kivy.require('1.9.0')

# the label widget is for rendering the text
from kivy.uix.label import Label

# to work with floatlayout first you have to import it
from kivy.uix.floatlayout import FloatLayout

# scatter is used to build interactive widgets that can be translated, rotated, and scaled with two or more fingers on a multitouch system
from kivy.uix.scatter import Scatter

# the textinput widgets provides a box for editable plain text
from kivy.uix.textinput import TextInput

# boxlayout arranges widgets in either vertical mode that is one on top of another or horizontal mode that is one after another
from kivy.uix.boxlayout import BoxLayout

# create the app class
class SamCodeHub(App):
    def build(self):
        b = BoxLayout(pos=(200, 400))
        
        # adding the text input
        t = TextInput(font_size= 50, size_hint_y=None, height=100)
        
        f = FloatLayout()
        
        # by scatter you are able to move the text on the screen to anywhere you want
        s = Scatter()
        
        l = Label(text="Hello!!!",font_size= 50)
        
        f.add_widget(s)
        s.add_widget(l)
        
        b.add_widget(t)
        b.add_widget(f)
        
        # binding it with Label
        t.bind(text= l.setter('text'))
        return b
    
# run the app
if __name__ == "__main__":
    SamCodeHub().run()