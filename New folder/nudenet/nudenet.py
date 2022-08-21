# pip install --upgrade nudenet
# import module
from nudenet import NudeClassifier

# initialize classifier
c = NudeClassifier()

# classify single image 
data = c.classify('image.jpg')
print(data)
# return {path_to_image}(safe:probability, unsafe; probablity)


