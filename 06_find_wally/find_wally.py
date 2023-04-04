"""
File: find Wally.py
Name: An Lee
----------------------------------
Combine the figure and background, then make whole new image left only two color: black and white.
Then make a maze with original background to hide the figure.
Let's play "find Wally" !
"""
from simpleimage import SimpleImage


def build_puzzle(background_img, comic_world):
    bg = background_img
    cw = comic_world
    # Create a bigger image to confuse player.
    big_puzzle = SimpleImage.blank(bg.width*2, bg.height*2)
    for y in range(bg.height):
        for x in range(bg.width):
            # Divide the new canvas into four parts, and hide the combine figure at II quadrant.
            bg_pixel = bg.get_pixel(x, y)
            cw_pixel = cw.get_pixel(x, y)
            # II quadrant: replaced by combine picture.
            big_puzzle_pixel_2 = big_puzzle.get_pixel(x, y)
            big_puzzle_pixel_2.red = cw_pixel.red
            big_puzzle_pixel_2.green = cw_pixel.green
            big_puzzle_pixel_2.blue = cw_pixel.blue
            # III quadrant: replaced by original background image.
            big_puzzle_pixel_3 = big_puzzle.get_pixel(x, y+bg.height-1)
            big_puzzle_pixel_3.red = bg_pixel.red
            big_puzzle_pixel_3.green = bg_pixel.green
            big_puzzle_pixel_3.blue = bg_pixel.blue
            # I quadrant: replaced by original background image.
            big_puzzle_pixel_1 = big_puzzle.get_pixel(x+bg.width-1, y)
            big_puzzle_pixel_1.red = bg_pixel.red
            big_puzzle_pixel_1.green = bg_pixel.green
            big_puzzle_pixel_1.blue = bg_pixel.blue
            # IV quadrant: replaced by original background image.
            big_puzzle_pixel_4 = big_puzzle.get_pixel(x+bg.width-1, y+bg.height-1)
            big_puzzle_pixel_4.red = bg_pixel.red
            big_puzzle_pixel_4.green = bg_pixel.green
            big_puzzle_pixel_4.blue = bg_pixel.blue
    return big_puzzle


def black_white(img):
    pic = img
    # In order to hide the colorful figure, we turn the whole image into a black and white world.
    for y in range(pic.height):
        for x in range(pic.width):
            pic_pixel = pic.get_pixel(x, y)
            if (pic_pixel.red+pic_pixel.green+pic_pixel.blue) > 500:
                pic_pixel.red = 255
                pic_pixel.green = 255
                pic_pixel.blue = 255
            else:
                pic_pixel.red = 0
                pic_pixel.green = 0
                pic_pixel.blue = 0
    return pic


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
            avg = (f_pixel.red+f_pixel.blue)//2
            # In every pixel in figure image, if its green value is higher than
            # the standard that we set then replace it with the pixel in background.
            # Upper green background too bright, we use different criteria to deal with it.
            if y < f.height // 1.82:
                if f_pixel.green > avg*1.35:
                    bg_pixel = bg.get_pixel(x, y)
                    f_pixel.red = bg_pixel.red
                    f_pixel.green = bg_pixel.green
                    f_pixel.blue = bg_pixel.blue
            else:
                if f_pixel.green > avg*1.6025:
                    bg_pixel = bg.get_pixel(x, y)
                    f_pixel.red = bg_pixel.red
                    f_pixel.green = bg_pixel.green
                    f_pixel.blue = bg_pixel.blue
    return f


def main():
    """
    Combine the figure and background, then make whole new image left only two color: black and white.
    Then make a maze with original background to hide the figure.
    Let's play "find Wally" !
    """
    find_wally = SimpleImage("images/starwar.png")
    figure = SimpleImage("images/An.png")
    find_wally.make_as_big_as(figure)
    result = combine(find_wally, figure)
    comic_world = black_white(result)
    puzzle = build_puzzle(find_wally, comic_world)
    puzzle.show()


if __name__ == '__main__':
    main()
