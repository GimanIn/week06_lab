#############################################
# Dimension Expansion using numpy
#############################################

import numpy as np
from PIL import Image

img = Image.open('../images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>

img_gray = img.convert('L')
# img_gray.show()

img_gray = np.array(img_gray)
print(np.shape(img_gray), img_gray.shape)
print(img_gray.dtype, img_gray.ndim)

# (680, 1024) -> H, W

# 2D -> 3D
img_gray_3d = img_gray[:, :, np.newaxis]
print(img_gray_3d.shape)  # H, W, C(=1)

img_gray_4d = img_gray_3d[np.newaxis, :, :, :]
print(img_gray_4d.shape)  # N(=1), H, W, C(=1)

# 4d -> 3d
img2_3d = img_gray_4d[0, :, :, :]
print(img2_3d.shape)

# 3D -> 2D
img2_2d = img2_3d[:, :, 0]
print(img2_2d.shape)



