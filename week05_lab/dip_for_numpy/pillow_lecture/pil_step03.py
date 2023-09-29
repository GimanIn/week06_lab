#############################################
# Color Image Split & Merge using PILLOW
#############################################

import numpy as np
from PIL import Image

img = Image.open('../images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>

# img.show()

print(type(img))
print(img.mode)
print(img.size)   # (1024, 680) --> W, H

bands = img.getbands()
print(bands)
print('------------------')

r, g, b = img.split()
print(r.size)
print(r.mode)
print(type(r))
print('==================')

# r.show()
# g.show()

np_r = np.array(r)
np_g = np.array(g)
np_b = np.array(b)

np_r[:, :] = 255
np_g[:, :] = 255
np_b[:, :] = 0

print('[INFO]np_r(shape) : ', np_r.shape)

r = Image.fromarray(np_r)
g = Image.fromarray(np_g)
b = Image.fromarray(np_b)

merge_img = Image.merge('RGB', (r, g, b))
merge_img.show()


# Numpy array 만드는 방법 (zeros, ones, empty)

# Question 1: Red Display (768, 1024, 3)

# Question 2: Green Display (768, 1024, 3)

# Question 3: Blue Display (768, 1024, 3)

# Question 4: Magenta Display (768, 1024, 3)



# print('=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/')
#
# np_img = np.array(img)
#
# print(np_img.shape)  # (680, 1024, 3) ---> H, W, C
# print(np_img.ndim)
# print(np_img.size)
# print(np_img.dtype)