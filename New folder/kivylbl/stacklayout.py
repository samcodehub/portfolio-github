# import kivy module
import kivy

# below this kivy version you cannot use the app
kivy.require("1.9.1")

# base class of your app
from kivy.app import App

# creates the button in kivy ,if not imported shows the error
from kivy.uix.button import Button

# The StackLayout arranges children vertically or horizontally, as many as the layout can fit.
from kivy.uix.stacklayout import StackLayout

# to change the kivy default setting we use config
from kivy.config import Config
Config.set('graphics','width','500')
Config.set('graphics','height','500')


# class in which we are creating StackLayout
class StackLayoutApp(App):
	
	def build(self):

		# Different orientation
		# ['lr-tb', 'tb-lr', 'rl-tb', 'tb-rl','lr-bt', 'bt-lr', 'rl-bt', 'bt-rl']	
		SL = StackLayout(orientation ='lr-tb')

		# Creating Multiple Buttons
		btn1 = Button(text ="B1",
					font_size = 20,
					size_hint =(.2, .1),
                    background_color =(0, 0.5, 0.5, 1))
		btn2 = Button(text ="B2",
					font_size = 20,
					size_hint =(.2, .1),
                    background_color =(0, 0.5, 0.5, 1))
		btn3 = Button(text ="B3",
					font_size = 20,
					size_hint =(.2, .1),
                    background_color =(0, 0.5, 0.5, 1))
		btn4 = Button(text ="B4",
					font_size = 20,
					size_hint =(.2, .1),
                    background_color =(0, 0.5, 0.5, 1))
		btn5 = Button(text ="B5",
					font_size = 20,
					size_hint =(.2, .1),
                    background_color =(0, 0.5, 0.5, 1))
		btn6 = Button(text ="B6",
					font_size = 20,
					size_hint =(.2, .1),
                    background_color =(0, 0.5, 0.5, 1))
		btn7 = Button(text ="B7",
					font_size = 20,
					size_hint =(.2, .1),
                    background_color =(0, 0.5, 0.5, 1))
		btn8 = Button(text ="B8",
					font_size = 20,
					size_hint =(.2, .1),
                    background_color =(0, 0.5, 0.5, 1))
		btn9 = Button(text ="B9",
					font_size = 20,
					size_hint =(.2, .1),
                    background_color =(0, 0.5, 0.5, 1))
		btn10 = Button(text ="B10",
					font_size = 20,
					size_hint =(.2, .1),
                    background_color =(0, 0.5, 0.5, 1))


		# adding widgets
		SL.add_widget(btn1)
		SL.add_widget(btn2)
		SL.add_widget(btn3)
		SL.add_widget(btn4)
		SL.add_widget(btn5)
		SL.add_widget(btn6)
		SL.add_widget(btn7)
		SL.add_widget(btn8)
		SL.add_widget(btn9)
		SL.add_widget(btn10)


		# returning widgets
		return SL

# Run the Kivy app
if __name__ == '__main__':
	StackLayoutApp().run()
 

