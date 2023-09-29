#############################################
# Image Concatnation
#############################################

import numpy as np
from PIL import Image

img = Image.open('../images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>

np_img = np.array(img)
print(np_img.shape)

np_img = np_img[np.newaxis, :, :, :]

np_img = np.concatenate((np_img, np_img), axis=0)
print(np_img.shape)

# img_t = Image.fromarray(np_img)
# img_t.show()