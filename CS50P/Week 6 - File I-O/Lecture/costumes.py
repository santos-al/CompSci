import sys

from PIL import Image

path = "/Users/santosal/Desktop/Code/CompSci/CS50P/Week 6 - File I-O/Lecture"

images = []

for arg in sys.argv[1:]:
    image = Image.open(path + "/" + arg)
    images.append(image)

images[0].save(
    path + "/costumes.gif",
    save_all=True,
    append_images=[images[1]],
    duration=200,
    loop=0
)