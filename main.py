# ImageDraw lets us draw on our image
# ImageColor will let us get the correct RGB values from color strings "red", "blue", etc
try:
    import Image
except ImportError:
    from PIL import Image

from draw_circle import draw_random_circle
# Colors we will be using in RGB values
red = (255, 0, 0)
green = (0, 204, 0)
blue = (0, 128, 255)

# Image.new(mode, size, color=0)
# mode is the color format: RGB, black/white, RGBA, floating point pixels, etc.
# http://pillow.readthedocs.io/en/5.2.x/handbook/concepts.html#concept-modes
# size is the (width, height) in pixels
# color: default is black.
mode = 'RGB'
size = (1920, 1080)
newImage = Image.new(mode, size, color=blue)

draw_random_circle(newImage, radius=200, in_border=True, fill=red, outline=0)
draw_random_circle(newImage, radius=200, in_border=True, fill=red, outline=0)
draw_random_circle(newImage, radius=200, in_border=True, fill=red, outline=0)
draw_random_circle(newImage, radius=200, in_border=True, fill=red, outline=0)

newImage.save('out.png', format='PNG')
