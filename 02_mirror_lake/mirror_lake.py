"""
File: mirror_lake.py
Name: An Lee
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original colored image.
    :return: SimpleImage, With doubling the original height, the new imagine size will be twice as the original one
             and combined by the original image and a mirror image.
    """
    img = SimpleImage(filename)
    # Build a blank image, which width is equal to the original image
    # and height is equal to the twice of the original image.
    blank_img = SimpleImage.blank(img.width, img.height*2)
    # Picking up every pixel and embed it into the right position of blank_img.
    for y in range(img.height):
        for x in range(img.width):
            # Define evey pixel's site in the original image.
            img_pixel = img.get_pixel(x, y)
            # Define evey pixel's site in the blank imagine's height.
            blank_pixel_h = blank_img.get_pixel(x, blank_img.height-y-1)
            # Get original pixel embed in the every pixel in blank image's height.
            blank_pixel_h.red = img_pixel.red
            blank_pixel_h.green = img_pixel.green
            blank_pixel_h.blue = img_pixel.blue
            # Define evey pixel's site in the blank image's width.
            blank_pixel_w = blank_img.get_pixel(x, y)
            # Get original pixel embed in the every pixel in blank image's width.
            blank_pixel_w.red = img_pixel.red
            blank_pixel_w.green = img_pixel.green
            blank_pixel_w.blue = img_pixel.blue
    return blank_img


def main():
    """
    Producing a lake-mirror liked effect on the original image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
