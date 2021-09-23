"""
File: blur.py
Name: An_Lee
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: str, the file path of the original background image.
    :return:SimpleImage, the blurred version of the original image.
    """
    original_img = img
    blur_it = SimpleImage.blank(original_img.width, original_img.height)
    for y in range(original_img.height):
        for x in range(original_img.width):
            red_sum = 0
            green_sum = 0
            blue_sum = 0
            time = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x+i
                    pixel_y = y+j
                    if 0 <= pixel_x < original_img.width:
                        if 0 <= pixel_y < original_img.height:
                            pixel = original_img.get_pixel(pixel_x, pixel_y)
                            red_sum += pixel.red
                            green_sum += pixel.green
                            blue_sum += pixel.blue
                            time += 1
            new_pixel = blur_it.get_pixel(x, y)
            new_pixel.red = red_sum / time
            new_pixel.green = green_sum / time
            new_pixel.blue = blue_sum / time
    return blur_it


def main():
    """
    This program can blurred the input image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
