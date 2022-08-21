# base class of your app
from kivy.app import App

# The AnchorLayout aligns its children to a border(top, bottom, left, right) or center
from kivy.uix.anchorlayout import AnchorLayout

# BoxLayout arranges children in a vertical or horizontal box,or help to put the childrens at the desired location.
from kivy.uix.boxlayout import BoxLayout

# creates the button in kivy
from kivy.uix.button import Button

# to change the kivy default setting we use config
from kivy.config import Config
Config.set('graphics','width','400')
Config.set('graphics','height','400')


# A Kivy app demonstrating the working of anchor layout
class AnchorLayoutApp(App):
	
	def build(self):

		
		# Anchor Layout, position, size_hint and background color
		layout = AnchorLayout(
		anchor_x ='left', anchor_y ='top')
		btn = Button(text ='AnchorLayout',
					size_hint =(.4, .1),
					background_color =(0, 0.5, 0.5, 1))
	
		layout.add_widget(btn)
		return layout

# creating the object root for AnchorLayoutApp() class
root = AnchorLayoutApp()
# Run the Kivy app
root.run()