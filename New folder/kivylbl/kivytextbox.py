import kivy

# base class of your app inherite from app class always refers to the instance of your application
from kivy.app import App

# class is the base class required for creationg widgets
from kivy.uix.widget import Widget

# the label widget is for rendering text
from kivy.uix.label import Label

# to use checkbox you must import it from checkbox module
from kivy.uix.checkbox import CheckBox

# the gridlayout arranges children in a matrix
from kivy.uix.gridlayout import GridLayout

# the config module is used to set the window size
from kivy.config import Config
Config.set('graphics','width','400')
Config.set('graphics','height','400')

# container class for the app's widgets
class check_box(GridLayout):
    def __init__(self, **kwargs):
        # super function can be used to gain access to inherited methodes from a parent or sibling class that has been overwritten in a class object
        super(check_box, self).__init__(**kwargs)
        
        # 3 rows in grid layout
        self.rows = 3
        
        # add checkbox, widgets and labels
        self.add_widget(Label(text='Kivy'))
        self.active = CheckBox(active = False)
        self.add_widget(self.active)
        
        self.add_widget(Label(text='Tkinter'))
        self.active = CheckBox(active = False)
        self.add_widget(self.active)
        
        self.add_widget(Label(text = 'Other'))
        self.active = CheckBox(active= False)
        self.add_widget(self.active)
        
# app derived from app class
class CheckBoxApp(App):
    def build(self):
        return check_box()
    
# run the app
if __name__ =='__main__':
    CheckBoxApp().run()
        