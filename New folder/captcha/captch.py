# pip install captcha  
from captcha.image import ImageCaptcha

# store the captcha in the image and set the dimensions
image = ImageCaptcha(width=200, height=90)

# generate method 
data = image.generate('samcodehub')

# write the captcha into the file 
image.write('samcodehub', 'demo.png')