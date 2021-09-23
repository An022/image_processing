"""
File: fire_alarm.py
Name: An Lee
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05
MAXIMUM_COLOR = 255


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original colored image.
    :return:The image with the fire area will be highlighted by full red
            while other safe areas' color will be turned into gray scale.
    """
    img = SimpleImage(filename)
    # Have to check evey pixel in imagine.
    for pixel in img:
        avg = (pixel.red+pixel.green+pixel.blue)//3
        # In the pixel, if its red value is higher than the standard that we set
        # turn the red value to maximum.
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = MAXIMUM_COLOR
            pixel.green = 0
            pixel.blue = 0
        # In the pixel, if its red value is lower than the standard that we set
        # turn each original color value to average of the original RGB value.
        else:
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return img


def main():
    """
    The program will check the imagine to see if there are any fire happened in the forest.
    If any area has a highly chance of having forest fire, the imagine will reflect the color with red
    On the contracts, those safe area's original color will be turned into gray scale.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
