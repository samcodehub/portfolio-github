# pip install stegano
from stegano import lsb

image = "image.jpg"
new_img = "hided_msg.png"

msg = "your secret message here"

# to hide the message
lsb.hide(image, message=msg).save(new_img)

# to reveal hidden message
message = lsb.reveal(new_img)
print('Hidden message:', message)