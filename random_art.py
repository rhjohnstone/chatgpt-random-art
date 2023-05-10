import random

from PIL import Image, ImageDraw

# create new image
width = 800
height = 800
image = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(image)

# define a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

# loop to draw random lines
for i in range(1000):
    # set random pen color
    color = random.choice(colors)

    # set random line width
    line_width = random.randint(1, 20)

    # set random line coordinates
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)

    # draw random line
    draw.line((x1, y1, x2, y2), fill=color, width=line_width)

# show image
image.show()
