#############################################
# Image Concatnation
#############################################

import numpy as np
from PIL import Image

img = Image.open('../images/monarch.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>

img.show()

np_img = np.array(img)
print('[INFO]np_img.shape : ', np_img.shape)

# (512, 768, 3)

np_img_copy = np_img.copy()

np_slice_img = np_img[300:400,300:400,:]
print('[INFO]np_slice_img.shape : ', np_slice_img.shape)

slice_img = Image.fromarray(np_slice_img)
slice_img.show()

# xnview
