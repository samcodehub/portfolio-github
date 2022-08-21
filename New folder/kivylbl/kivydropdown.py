import kivy

# base class of your application inherites from app class always refers to the instance of your app
from kivy.app import App

# below this kivy version you cannot use the app
kivy.require('1.9.0')

# importing dropdown from the module to use in the program
from kivy.uix.dropdown import DropDown

# the button is a label with associated actions that are triggered when the button is pressed
from kivy.uix.button import Button

# another way to run kivy app
from kivy.base import runTouchApp

# create a dropdown with 5 buttons
dropdown = DropDown()
for index in range(5):
    # adding button in dropdown list
    btn = Button(text = 'Option % d'% index, background_color=(1,1,255), size_hint_y = None, height = 50)
    
    # binding the button to show the text when selected
    btn.bind(on_release = lambda btn: dropdown.select(btn.text))
    
    # then add the button inside the dropdown
    dropdown.add_widget(btn)

# create a menu button
mainbutton = Button(text = 'Menu', font_size = 30, background_color = (1,0,255), size_hint =(None, None), height= 60, width = 150, pos = (15, 500))

# show the dropdown menu when the mainbutton is released
mainbutton.bind(on_release = dropdown.open)

# listen for the selection in dropdown list and assign the option to the button text
dropdown.bind(on_select = lambda instance, x: setattr(mainbutton, 'text', x))

# runtouchApp
runTouchApp(mainbutton)