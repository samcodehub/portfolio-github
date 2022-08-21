# to change the kivy default setting we use config
from kivy.config import Config
Config.set('graphics','width','500')
Config.set('graphics','height','500')

# if you use the callback class to call rendering methods of another toolkit, you will have issues with the OpenGL context
from kivy.graphics import RenderContext

# a widget is the base building block of gui interfaces in kivy 
from kivy.uix.widget import Widget

# the Image widget is used to display images
from kivy.uix.image import Image

# base class of your app
from kivy.app import App

# this module contains the kivy core functionality and is not intended for end users
from kivy.base import EventLoop

class CustomShaderWidget(Widget):
    def __init__(self, **kwargs):
        # we must do this if no other widget has been loaded the GL context may not be fully prepared
        EventLoop.ensure_window()
        # most likely you will want to use the parent projection and modelview in order for your widget to behave the same as the rest of the widget
        self.canvas = RenderContext(use_parent_projection = True, use_parent_modelview = True)
        
        # declare glsl file path
        self.canvas.shader.source = 'myshader.glsl'
        super(CustomShaderWidget, self).__init__(**kwargs)
        
class CustomShaderApp(App):
    def build(self):
        shader_widget = CustomShaderWidget()
        im = Image(source = 'pic.png')
        shader_widget.add_widget(im)
        shader_widget.bind(size = im.setter('size'))
        return shader_widget
    
# run the app
if __name__ == '__main__':
    CustomShaderApp().run()