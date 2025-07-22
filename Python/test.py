from PIL import Image
import numpy as np


data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
img = Image.fromarray(data, "RGB")

img.save("image.png")
img.show()
