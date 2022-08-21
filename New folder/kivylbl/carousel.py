import kivy

# below this kivy version you can not use the app
kivy.require('2.0.0')

# base class of your app inherite from app class always refers to the instance of your application
from kivy.app import App

#The Carousel widget provides the classic mobile-friendly carousel view where you can swipe between slides
from kivy.uix.carousel import Carousel

# The Image widget is used to display an image this module contain all features of images 
from kivy.uix.image import AsyncImage

# the sourse of images. it could be local like now or the external link
src =["image/1.png","image/2.png","image/3.png","image/4.png","image/5.png"]

# Create the App class
class CarouselApp(App):
    def build(self):
        # Add carousel And add the direction of swipe
        carousel = Carousel(direction ='right')
        # Adding 5 slides
        for i in range(5):
            
            # using Asynchronous image
            image = AsyncImage(source = src[i], allow_stretch = True)
            carousel.add_widget(image)
        return carousel
    
# Run the App
if __name__ == '__main__':
    CarouselApp().run()