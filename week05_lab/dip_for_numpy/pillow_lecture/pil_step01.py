#############################################
# Image Read & Show
#############################################

import numpy as np
from PIL import Image

image = Image.open('../images/img_048.png')
print(type(image))

# image.show()

np_img = np.array(image)
print(type(np_img))
print(np_img.shape, np_img.ndim, np_img.size, np_img.dtype)
# (680, 1024, 3) --> H, W, C

# image2 = Image.fromarray(np_img)
# print(type(image2))

# image2.save('step01.png', 'png')

# image2.show()





