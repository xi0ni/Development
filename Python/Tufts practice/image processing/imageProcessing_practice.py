from PIL import Image
import numpy as np
import random
from matrices import d2, d4, d8, d16

# img = Image.new("RGB", (300, 300), "red")
# img.save("image.png")
# img = Image.open("Unknown.jpeg")
img = Image.open("lighthouse.png")
max = 255

img.show()

'''
print(np_img[0]) # entire row,column
print(np_img[0, 0]) # entire pixel
print(np_img[0, 0, 0]) # individual color channel (like red)"""
'''
# shifting color
"""
np_img = np.array(img)
np_img += 50
np.clip(np_img, 0, max)

Image.fromarray(np_img).show()"""

# turning it into grey scale and also reducing color intensity. bringing it closer to grey
"""
grey_img = img.convert("L")
t = 0.5
grey_img = np.array(img.convert("L"))
for y in range(grey_img.shape[0]):
    for x in range(grey_img.shape[1]):
        grey_img[y, x] = (t * grey_img[y, x]) + ((1 - t) * 127)
Image.fromarray(grey_img).show()
"""
# reducing color intensity. bringing it closer to grey
"""
t = 0.2
img = np.array(img)
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        img[y, x, 0] = (t * img[y, x, 0]) + ((1 - t) * 127)
        img[y, x, 1] = (t * img[y, x, 1]) + ((1 - t) * 127)
        img[y, x, 2] = (t * img[y, x, 2]) + ((1 - t) * 127)
Image.fromarray(img).show()
"""

# dithering tool. makes the image black and white. this one only works for greyscale


"""grey_img = np.array(img.convert("L"))
for y in range(grey_img.shape[0]):
    for x in range(grey_img.shape[1]):
        if grey_img[y, x] > 80:
            grey_img[y, x] = max
        else:
            grey_img[y, x] = 0
Image.fromarray(grey_img).show()
"""
# dithering tool for any image need to work on it
"""
img = np.array(img)
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        if img[y, x, 0] > [0, 0, 127]:
            img[y, x] = max
        if img[y, x, 1] > (0, 0, 127):
            img[y, x] = max
        if img[y, x, 2] > (0, 0, 127):
            img[y, x] = max

Image.fromarray(img).show()
"""
# random dithering
"""
grey_img = np.array(img.convert("L"))
for y in range(grey_img.shape[0]):
    for x in range(grey_img.shape[1]):
        num = random.randint(0, 256)
        if grey_img[y, x] > num:
            grey_img[y, x] = max
        else:
            grey_img[y, x] = 0
Image.fromarray(grey_img).show()
"""

# ordered dithering 2x2
"""
grey_img = np.array(img.convert("L"))

for y in range(0, grey_img.shape[0], 2):
    for x in range(0, grey_img.shape[1], 2):
        order = d2[y % 2, x % 2]
        if grey_img[y, x] > order:
            grey_img[y, x] = max
        else:
            grey_img[y, x] = 0


Image.fromarray(grey_img).show()
"""
# ordered dithering 4x4
"""
grey_img = np.array(img.convert("L"))

for y in range(0, grey_img.shape[0], 4):
    for x in range(0, grey_img.shape[1], 4):
        order = d4[y % 4, x % 4]
        if grey_img[y, x] > order:
            grey_img[y, x] = max
        else:
            grey_img[y, x] = 0


Image.fromarray(grey_img).show()
"""
# ordered dithering variable
d = d2
mod = d.shape[0]

grey_img = np.array(img.convert("L"))

for y in range(0, grey_img.shape[0], 4):
    for x in range(0, grey_img.shape[1], 4):
        order = d[y % mod, x % mod]
        if grey_img[y, x] > order:
            grey_img[y, x] = max
        else:
            grey_img[y, x] = 0


Image.fromarray(grey_img).show()


