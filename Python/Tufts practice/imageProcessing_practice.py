from PIL import Image
import numpy as np


# img = Image.new("RGB", (300, 300), "red")
# img.save("image.png")
img = Image.open("gradient_image.png")
grey_img = img.convert("L")

np_img = np.array(img)


"""print(np_img[0]) # entire row,column
print(np_img[0, 0]) # entire pixel
print(np_img[0, 0, 0]) # individual color channel (like red)"""
img.show()

np_img += 50
np.clip(np_img, 0, 255)

Image.fromarray(np_img).show()
