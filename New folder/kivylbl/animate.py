# import kivy module
import kivy

# below this kivy version you cannot use the app
kivy.require('1.0.7')

# animation is a way to make figures,images and widgets appear as moving in kivy
from kivy.animation import Animation

# base class of your app
from kivy.app import App

# creates the button in kivy
from kivy.uix.button import Button

# to change the kivy default setting we use config
from kivy.config import Config
Config.set('graphics','width','500')
Config.set('graphics','height','500')

# set the window background color
from kivy.core.window import Window
Window.clearcolor = (0.2, 0, .1, 1)

# make an app by deriving from the app class
class TestApp(App):
    
    def animate(self, instance):
        # create an animation object ,this object could be stored and reused each call or reused across diffrent widgets.
        # +- is a sequential step, while &= is in parallel
        animation = Animation(pos = (100, 100), t = 'out_bounce')
        animation += Animation(pos = (200, 100), t = 'out_bounce')
        animation &= Animation(size = (300, 300))
        animation += Animation(size = (100, 50))
        
        # apply the animation on the button, passed in the "instance" argument
        # notice that default 'click' animation (changing the button color while the mouse is down) is unchanged
        animation.start(instance)
        
    def build(self):
        # create a button, and attach animate() method as on_press handler
        button = Button(size_hint = (None, None), text = 'plop', background_color = (0, 1, .5), on_press=self.animate)
        return button
    
# run the app
if __name__ == '__main__':
    TestApp().run()