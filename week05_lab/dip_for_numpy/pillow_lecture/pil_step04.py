#############################################
# Convert Color image to Gray image using PILLOW
#############################################

import numpy as np
from PIL import Image

img = Image.open('../images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>

img_gray = img.convert('L')
# img_gray.show()

img_gray = np.array(img_gray)

# using numpy
def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = (1/3.0) * r + (1/3.0) * g + (1/3.0) * b
    # gray = (299 / 1000) * r + (587 / 1000) * g + (114 / 1000) * b
    return gray

np_img = np.array(img)

np_gray_img = rgb2gray(np_img)
gray_img = Image.fromarray(np_gray_img)
# gray_img.show()

print(np.allclose(img_gray, np_gray_img))


