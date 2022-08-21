# import module
import kivy

# base class of your app
from kivy.app import App

# The PageLayout class is used to create
# a simple multi-page layout,
from kivy.uix.pagelayout import PageLayout

# creates the button in kivy
from kivy.uix.button import Button

# to change the kivy default setting we use config
from kivy.config import Config

Config.set('graphics','width','400')
Config.set('graphics','height','400')
# creating the app class
class PageLayout(PageLayout):
	

	def __init__(self):
		
		# The super function in Python can be
		# used to gain access to inherited methods
		# which is either from a parent or sibling class.
		super(PageLayout, self).__init__()
  

		# creating buttons on different pages
        
		btn1 = Button(text ='Page 1', background_color = (0, 1, .5))
		
		btn2 = Button(text ='Page 2', background_color = (1, 1, .5))

		btn3 = Button(text ='Page 3', background_color = (0, .5, .5))
        
        
		# adding button on the screen
		# by add widget method
		self.add_widget(btn1)

		self.add_widget(btn2)

		self.add_widget(btn3)


# creating the App class
class Page_LayoutApp(App):
	

	def build(self):
		
		return PageLayout()
# Run the App
if __name__ == '__main__':
	Page_LayoutApp().run()
