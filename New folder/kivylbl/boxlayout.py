import kivy

# to choose the colors randomly every time you run it shows different colors
import random

# below this kivy version you cannot use the app
kivy.require('1.9.1')

# base class of your application inherites from app class always refers to the instance of your app
from kivy.app import App

# creates the button in kivy if not imported shows error
from kivy.uix.button import Button

# boxlayout arranges children in a vertical or horizontal box
from kivy.uix.boxlayout import BoxLayout

# declaring the colorse you can use directly also
red = [1,0,0,1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

# class in which we create the button
class BoxLayoutApp(App):
    def build(self):
        # to position oriented widgets again in the proper orientation use the vertical orientation to set all widgets
        superBox = BoxLayout(orientation = 'vertical')
        
        # to position widgets next to each other use a horizontal boxlayout
        HB = BoxLayout(orientation = 'horizontal')
        
        colors = [red, green, blue, purple]
        
        # styling the button boxlayout
        btn1 = Button(text = 'One', background_color = random.choice(colors), font_size = 32, size_hint = (0.5, 1))
        
        btn2 = Button(text = 'Two', background_color = random.choice(colors),font_size = 32, size_hint = (0.5, 1))
        
        HB.add_widget(btn1)
        HB.add_widget(btn2)
        
        # to position widgets above/below each other use vertical BoxLayout
        VB = BoxLayout(orientation = 'vertical')
        
        btn3 = Button(text = 'Three', background_color = random.choice(colors), font_size = 32, size_hint = (1, 10))
        
        btn4 = Button(text ='Four', background_color = random.choice(colors), font_size = 32, size_hint = (1, 15))
        
        VB.add_widget(btn3)
        VB.add_widget(btn4)
        
        # superbox used to align the oriented widgets
        superBox.add_widget(HB)
        superBox.add_widget(VB)
        
        return superBox
    
# creating the object root for Boxlayoutapp() class
root = BoxLayoutApp()

# run function runs the whole program
root.run() 