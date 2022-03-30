from PIL import Image
from math import floor


def mandelbrot(c: complex, iterations: int, threshold=16):
    """
    Returns the number of iterations the function endures the
    Mandelbrot function before diverging above a given threshold.
    """
    z = complex(0, 0)
    for i in range(iterations):
        z = z*z + c
        if z.real*z.real + z.imag*z.imag > threshold:
            break

    return i


def map_to_plane(img_x: float, img_y: float, img_width, img_height, min_x=-2, max_x=1, min_y=-1.5, max_y=1.5):
    return complex(
        (img_x / img_width) * (max_x-min_x) + min_x,
        -((img_y / img_height) * (max_y-min_y) + min_y)
    )


def render_mandelbrot(width: int, height: int,
                      x_offset=0, y_offset=0, zoom=1, iterations=100, threshold=16) -> Image.Image:
    """
    Returns a PIL image containing the Mandelbrot set
    rendered according to the passed arguments.
    """

    im = Image.new("HSV", (width, height))
    for y in range(height):
        for x in range(width):
            pos = map_to_plane(x, y, width, height, (-2/zoom) + x_offset,
                               (1/zoom) + x_offset, (-1.5/zoom) - y_offset, (1.5/zoom) - y_offset)
            m = mandelbrot(pos, iterations, threshold)/iterations
            color_value = int(floor(255*m))
            im.putpixel((x, y), (color_value, 255, 255))

    return im.convert("RGB")
