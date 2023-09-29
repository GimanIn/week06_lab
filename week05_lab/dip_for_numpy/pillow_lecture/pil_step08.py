#############################################
# Image Concatnation
#############################################

import numpy as np
from PIL import Image

img = Image.open('../images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>
img.show()

np_img = np.array(img)

np_img_reverse = 255 - np_img

img_reverse = Image.fromarray(np_img_reverse)
img_reverse.show()
