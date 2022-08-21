# pip install sketchpy
from sketchpy import canvas

obj = canvas.sketch_from_svg('bean.svg',scale=250)

obj.draw()