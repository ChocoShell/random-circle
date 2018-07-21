try:
    import ImageDraw
except ImportError:
    from PIL import ImageDraw

from random import randint

def draw_random_circle(image, radius=None, in_border=True, outline=None, fill=None):
    """
    Draws a circle at a random location in the image of a random or given size.
        Image: image to draw circle on
        radius: given radius of circle, will be chosen at random if not given
        outline, fill: parameters passed to ImageDraw.ellipse function
    """
    size_x, size_y = image.size
    radius = radius if radius else randint(0, size_y/2 if size_y < size_x else size_x/2)
    center_x = randint(0, size_x)
    center_y = randint(0, size_y)
    center = (center_x, center_y)

    draw_circle(image, center, radius, outline=outline, fill=fill, verbose=False)

def draw_circle(image, center, radius, in_border=True, verbose=True, outline=None, fill=None):
    """
    Draws a circle at given position "center" with the given radius on the given image.
        image: image to draw on
        center: tuple determing position of center circle
        radius: int determining radius of circle
        in_border: whether or not the whole circle should be in the image.
        verbose: Determines where it prints messages or not
        outline: outline parameter passed to ImageDraw.ellipse function
        fill: fill parameter passed to ImageDraw.ellipse function
    """
    try:
        # Making sure the center and radius sizes are within our image bounds.
        size_x, size_y = image.size
        if (center[0] <= size_x and
            center[1] <= size_y and
            radius <= size_x and
            radius <= size_y):

            x0 = center[0] - radius
            y0 = center[1] - radius
            x1 = center[0] + radius
            y1 = center[1] + radius

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
            draw.ellipse([(x0, y0), (x1, y1)], outline=outline, fill=fill)

            if verbose:
                print("Completed Successfully")
    except Exception as e:
        print(e)
