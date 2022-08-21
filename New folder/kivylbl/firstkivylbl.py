# import kivy module
import kivy

# below this kivy version you can not use the app or software
kivy.require("1.9.1")

# base class of your app inherite from app class app alwayes refers to the instance of your application
from kivy.app import App

# if you not import label and use it it will return error
from kivy.uix.label import Label

# defining the app class
class MyLabelApp(App):
    def build(self):
        # label to show the text on screen
        lbl = Label(text ="Label is added on screen :x:x",font_size=30, color=("yellow"))
        return lbl
# creating the object
label = MyLabelApp()
# run the window
label.run()
