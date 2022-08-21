# Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
import wikipedia

#The OS module in Python provides functions for interacting with the operating system.
import os

# importing kivy module
import kivy

# to change the default setting in kivy we use config
from kivy.config import Config

# change the app window size
Config.set('graphics','width','500')
Config.set('graphics','height','500')

# Core class for creating the default Kivy window.
from kivy.core.window import Window

# change the main window background color
Window.clearcolor = (0, .2, .2, .1)

# base class of your app inherite from app class app alwayes refers to the instance of your application
from kivy.app import App

# The Label widget is for rendering text
from kivy.uix.label import Label

# The GridLayout arranges children in a matrix. It takes the available space and divides it into columns and rows, then adds widgets to the resulting “cells”.
from kivy.uix.gridlayout import GridLayout

# The Button is a Label with associated actions that are triggered when the button is pressed (or released after a click/touch)
from kivy.uix.button import Button

# The TextInput widget provides a box for editable plain text.
from kivy.uix.textinput import TextInput

# the Kivy clock attempts to execute any scheduled callback rhythmically as determined by the specified fps (frame per second, see maxfps in config ).
from kivy.clock import Clock

# The screen manager is a widget dedicated to managing multiple screens for your application.
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition

# The ScrollView manages the position of its children similarly to a RelativeLayout but does not use the size_hint .
from kivy.uix.scrollview import ScrollView

# The Popup widget is used to create modal popups.
from kivy.uix.popup import Popup

# select button class. it prepare all similar titles as a button to select, we declared the font_size , size_hint , height/width and background color of it
class SelectBtn(Button):
    def __init__(self, **kwargs):
        super(SelectBtn, self).__init__(**kwargs)
        self.font_size = '20px'
        self.size_hint_x = None
        self.height = Window.height/4.0
        self.width = Window.width/1.5
        self.background_color = (.5,.5,1)
        
# the popup shows all available options ,we declared a popup title and a bar to show the scrolling, we have two color for it states as active and inactive  and position it on right side     
class SelectSearch(Popup):
    def __init__(self, search_param=0,
                 _parent=0, a=0, **kwargs):
        super(SelectSearch, self).__init__(**kwargs)
        self._parent = _parent
        self.title = 'Select Your Title From Available Options'
        self.layout = ScrollView(
            scroll_type=['bars'],
            bar_width='10px',
            size=(Window.width, Window.height),
            pos_hint={'center_x': .5},
            bar_color=([.1, .55, .55, 1]),  
            bar_inactive_color=([.1, .7, .17, 1]))  
        
        self.grid = GridLayout(
            size_hint=(None, 2),
            cols=1
        )
        self.search_param = search_param
        for i in search_param:
            self.btn = SelectBtn()
            self.btn.text = i
            self.btn.bind(on_press=self.callback)
            self.grid.add_widget(self.btn)
        self.layout.add_widget(self.grid)
        self.add_widget(self.layout)
    
    def callback(self, event):
        self.dismiss()
        self._parent.search(event.text, self.search_param)

# search button class a create the button        
class SearchG(Screen):
    def __init__(self, **kwargs):
        super(SearchG, self).__init__(**kwargs)
        self.wait_time = 0.2
        self.pos_in_text = 0
        self.paused = False
        self.searchbtn = Button(text="Search",font_size='30px',pos_hint={'center_x':.5, 'center_y':.5},size_hint=(None, None),size=(Window.width/3, Window.height/8),background_color =(0.5,1,0,1))   
        self.searchbtn.bind(on_press=self.search1)
        self.add_widget(self.searchbtn)
        # creating up speed button to turn the velocity of showing words
        self.upspeedbtn = Button(text="+",
                          font_size='50px',
                          pos_hint={'center_x':.9, 'center_y':.9},
                          size_hint=(None, None),
                          size=(Window.width/8, Window.height/8),background_color =(1,1,.1,1))
        self.upspeedbtn.bind(on_press=self.upspeed)
        
        # creating down speed button to turn down velocity of showing words
        self.downspeedbtn = Button(text="-",
                          font_size='80px',
                          pos_hint={'center_x':.9, 'center_y':.77},
                          size_hint=(None, None),
                          size=(Window.width/8, Window.height/8),background_color = (1,.2,0,.7))
        self.downspeedbtn.bind(on_press=self.downspeed)
        
        # creating pause button to pause the words anytime you want and play it again by pressing again
        self.pausebtn = Button(text="Pause",
                          font_size='30px',
                          pos_hint={'center_x':.2, 'center_y':.1},
                          size_hint=(None, None),
                          size=(Window.width/3, Window.height/8),background_color = (1,.6,.2,1))
        self.pausebtn.bind(on_press=self.pause)
        
        # creatint a textinput to recieve get the input from the user
        self.txt = TextInput(text="",
                          font_size='30px',
                          pos_hint={'center_x':.5, 'center_y':.7},
                          size_hint=(None, None),
                          size=(Window.width/1.5, Window.height/9))
        self.add_widget(self.txt)
        # creating a label on the center of window to render the results
        self.text_label = Label(text="",
                          font_size='60px',
                          pos_hint={'center_x':.5, 'center_y':.5},
                          size_hint=(None, None),
                          size=(Window.width/4, Window.height/6))
        
        # creating the stop button to stop the rendering text and return to main page
        self.stopbtn = Button(text="Stop",
                          font_size='30px',
                          pos_hint={'center_x':.8, 'center_y':.1},
                          size_hint=(None, None),
                          size=(Window.width/3, Window.height/8),background_color = (1,.1,.1,.7))
        self.stopbtn.bind(on_press=self.stop)
        
    # search function to get the data from wikipedia and show it
    def search1(self, event):
        a = wikipedia.search(str(self.txt.text))
        popup = SelectSearch(a, self)
        popup.open()
    def search(self, position, a):
        if self.pos_in_text == 0:
            # split the results into words
            self.content = ((wikipedia.page(a[a.index(position)]).content).split())
            self.remove_widget(self.searchbtn)
            self.remove_widget(self.txt)
            self.remove_widget(self.downspeedbtn)
            self.remove_widget(self.upspeedbtn)
            self.remove_widget(self.pausebtn)
            self.remove_widget(self.stopbtn)
            self.add_widget(self.downspeedbtn)
            self.add_widget(self.upspeedbtn)
            self.add_widget(self.pausebtn)
            self.add_widget(self.text_label)
            self.add_widget(self.stopbtn)
        Clock.unschedule(self.read_text)
        Clock.schedule_interval(self.read_text, self.wait_time)
        
    # declaring all used functions
    def read_text(self, dt):
        self.text_label.text = self.content[self.pos_in_text]
        self.pos_in_text += 1
    def upspeed(self ,event):
        self.wait_time -= .1
        Clock.unschedule(self.read_text)
        Clock.schedule_interval(self.read_text, self.wait_time)
    def downspeed(self, event):
        self.wait_time += .1
        Clock.unschedule(self.read_text)
        Clock.schedule_interval(self.read_text, self.wait_time)
    def pause(self, event):
        if self.paused:
            Clock.schedule_interval(self.read_text, self.wait_time)
            self.paused = False
        else:
            self.paused = True
            Clock.unschedule(self.read_text)
    def stop(self, event):
        self.remove_widget(self.searchbtn)
        self.remove_widget(self.txt)
        self.remove_widget(self.downspeedbtn)
        self.remove_widget(self.upspeedbtn)
        self.remove_widget(self.pausebtn)
        self.remove_widget(self.stopbtn)
        self.remove_widget(self.text_label)
        self.add_widget(self.searchbtn)
        self.add_widget(self.txt)
        self.pos_in_text = 0
        Clock.unschedule(self.read_text)
        
# creating the wikipedia app
class WikiPediaApp(App):
    def __init__(self, **kwargs):
        super(WikiPediaApp, self).__init__(**kwargs)
    def build(self):
        sm.add_widget(SearchG(name='search'))
        return sm
    
# run the app
if __name__ == ("__main__"):
    sm = ScreenManager(transition=NoTransition())
    WikiPediaApp().run()
