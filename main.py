# ImageDraw lets us draw on our image
# ImageColor will let us get the correct RGB values from color strings "red", "blue", etc
try:
    import Image
except ImportError:
    from PIL import Image
import csv
from draw_circle import draw_random_circle
# Colors we will be using in RGB values
red = (255, 0, 0)
green = (0, 204, 0)
blue = (0, 128, 255)
white = (255, 255, 255)

# Image.new(mode, size, color=0)
# mode is the color format: RGB, black/white, RGBA, floating point pixels, etc.
# http://pillow.readthedocs.io/en/5.2.x/handbook/concepts.html#concept-modes
# size is the (width, height) in pixels
# color: default is black.
mode = 'RGB'
size = (100, 75)
# path = "E:/Users/Jonathan/Coding/Machine-Learning/tensorflow-tutorial/experiment/object-position-recognition/data/large"
path = './data'
num_image = 1000

with open('data.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    header = ['Filename', 'Coordinates']
    a.writerow(header)
    
for i in range(num_image):
    img = Image.new(mode, size, color=white)
    coords = draw_random_circle(img, in_border=True, fill=red)
    if coords:
        coords = coords if not type(coords[0]) == tuple else list(sum(coords, ()))
        filename = f"image{i}"
        img.save(f"{path}/{filename}.png", "PNG")
        with open('data.csv', 'a', newline='') as fp:
            a = csv.writer(fp, delimiter=',')
            a.writerow([filename, " ".join([str(x) for x in coords])])
