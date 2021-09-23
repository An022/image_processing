"""
File: green_screen.py
Name: An Lee
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: str, the file path of the original background image.
    :param figure_img: str, the file path of the original figure image.
    :return: Replace the green background in figure imagine into the background imagine.
    """
    bg = background_img
    f = figure_img
    # Define evey pixel's site in the figure imagine.
    for y in range(f.height):
        for x in range(f.width):
            f_pixel = f.get_pixel(x, y)
            bigger = max(f_pixel.red, f_pixel.blue)
            # In every pixel in figure image, if its green value is higher than
            # the standard that we set then replace it with the pixel in background.
            if f_pixel.green > 2 * bigger:
                bg_pixel = bg.get_pixel(x, y)
                f_pixel.red = bg_pixel.red
                f_pixel.green = bg_pixel.green
                f_pixel.blue = bg_pixel.blue
    return f


def main():
    """
    Without showing the green background in the figure, print the combine imagine
    of the original figure and original the background.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
