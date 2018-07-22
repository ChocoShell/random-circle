try:
    import ImageDraw
except ImportError:
    from PIL import ImageDraw

from random import randint

def draw_random_circle(image, diameter=None, in_border=True, outline=None, fill=None):
    """
    Draws a circle at a random location in the image of a random or given size.
        Image: image to draw circle on
        radius: given radius of circle, will be chosen at random if not given
        outline, fill: parameters passed to ImageDraw.ellipse function
    """
    size_x, size_y = image.size

    fill = fill if fill else (randint(0, 256), randint(0, 256), randint(0, 256))

    diameter = diameter if diameter else randint(0, min(size_y, size_x)-1)
    
    start_x = randint(0, size_x-diameter-1)
    start_y = randint(0, size_y-diameter-1)
    start = (start_x, start_y)

    return draw_circle(image, start, diameter, in_border=in_border, outline=outline, fill=fill, verbose=False)

def draw_circle(image, start, diameter, in_border=True, verbose=True, outline=None, fill=None):
    """
    Draws a circle at given position "center" with the given radius on the given image.
        image: image to draw on
        start: tuple determing position of where to begin bounding box of circle
        diameter: int determining diameter of circle
        in_border: whether or not the whole circle should be in the image.
        verbose: Determines where it prints messages or not
        outline: outline parameter passed to ImageDraw.ellipse function
        fill: fill parameter passed to ImageDraw.ellipse function
    """
    try:
        # Making sure the center and radius sizes are within our image bounds.
        size_x, size_y = image.size
        x0, y0 = start
        if (x0 + diameter <= size_x and
            y0 + diameter <= size_y):

            x1 = x0 + diameter
            y1 = y0 + diameter

            if in_border:
                # Setting bounds so the entire circle remains in the image
                if x0 < 0:
                    x1 -= x0
                    x0 = 0

                if y0 < 0:
                    y1 -= y0
                    y0 = 0

                if x1 > size_x:
                    x0 -= x1 - size_x
                    x1 = size_x

                if y1 > size_y:
                    y0 -= y1 - size_y
                    y1 = size_y

            # Draw handler for our image
            draw = ImageDraw.Draw(image)

            # draw.ellipse(xy, fill=None, outline=None)
            # Draws an ellipse inside the given bounding box.
            # xy can either be:
            #   [(x0, y0), (x1, y1)] or 
            #   [x0, y0, x1, y1]
            #   where x1 >= x0 and y1 >= y0.
            draw.ellipse([x0, y0, x1, y1], outline=outline, fill=fill)

            if verbose:
                print("Completed Successfully")
            return [(x0, y0), (x1, y1)]
        else:
            print(x0, y0, diameter)
    except Exception as e:
        print(e)
