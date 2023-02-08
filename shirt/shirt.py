import os
import sys
from PIL import Image, ImageOps

if len(sys.argv) != 3 or not os.path.isfile(sys.argv[1]):
    if not sys.argv[1].endswith(('.png','.jpg', '.jpeg')):
        sys.exit("Not two commands or invalid extension")

image = Image.open(sys.argv[1])
shirt = Image.open('shirt.png')
size = shirt.size
fitted = ImageOps.fit(image, size)
fitted.paste(shirt, shirt)
fitted.save(sys.argv[2])

input_name, input_ext = os.path.splitext(sys.argv[1])
output_name, output_ext = os.path.splitext(sys.argv[2])
if input_ext != output_ext:
    sys.exit('Not same file type')