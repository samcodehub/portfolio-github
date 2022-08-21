# pip install moviepy

from moviepy.editor import *

# loading the video 
clip = VideoFileClip("video.mp4")

# getting the first 5 seconds of the video
clip = clip.subclip(0, 5)

# cutting out some part of the video  
clip = clip.cutout(2, 4)

# showing the clip 
clip.ipython_display(width = 360)