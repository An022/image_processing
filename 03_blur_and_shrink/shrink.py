"""
File: shrink.py
Name: An Lee
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original colored image.
    :return img: SimpleImage, the shrink imagine with 1/2 width and 1/2 height of original img.
    """
    img = SimpleImage(filename)
    # Create an empty canvas with 1/2 width and 1/2 height of original img.
    small_img = SimpleImage.blank(img.width//2, img.height//2)
    # Define evey pixel's site in the figure imagine.
    for y in range(img.height):
        for x in range(img.width):
            img_pixel = img.get_pixel(x, y)
            # For the small_img, we just pick those pixel sited 1/2 width and 1/2 height of original img.
            small_img_pixel = small_img.get_pixel(x//2, y//2)
            # Get original pixel embed in new empty canvas.
            small_img_pixel.red = img_pixel.red
            small_img_pixel.green = img_pixel.green
            small_img_pixel.blue = img_pixel.blue
    return small_img


def main():
    """
    This function present a new shrink imagine which has 1/2 width and 1/2 height of original imagine.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
