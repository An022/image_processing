"""
File: mini_pohtoshop
----------------------------------------------
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
Name: An Lee
-----------------------------------------------

We compare a series of pictures, then renew the pixel to erase the pedestrian in the photo.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values
    """
    # get pixel's RGB.
    pixel_red = pixel.red
    pixel_green = pixel.green
    pixel_blue = pixel.blue
    # Calculate the color distance between pixel and the mean RGB.
    color_distance = ((red-pixel_red)**2 + (green-pixel_green)**2 + (blue-pixel_blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    rgb = []
    # Get every rgb value in list of pixel to sum up.
    for i in range(len(pixels)):
        sum_red += pixels[i].red
        sum_green += pixels[i].green
        sum_blue += pixels[i].blue
    # Calculate each rgb's average value.
    avg_red = sum_red / len(pixels)
    avg_green = sum_green / len(pixels)
    avg_blue = sum_blue / len(pixels)
    if sum_red == 0:
        avg_red = 0
    if sum_green == 0:
        avg_green = 0
    if sum_blue == 0:
        avg_red = 0
    # Add the result of each rgb's average in rgb's list.
    rgb.append(int(avg_red))
    rgb.append(int(avg_green))
    rgb.append(int(avg_blue))
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    best = pixels[0]
    min_color_distance = 255
    avg_rgb = get_average(pixels)
    for i in range(len(pixels)):
        color_distance = get_pixel_dist(pixels[i], avg_rgb[0], avg_rgb[1], avg_rgb[2])
        if color_distance < min_color_distance:
            min_color_distance = color_distance
            best = pixels[i]
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    # Run through every pixel in the "result" to get the best pixel.
    for y in range(height):
        for x in range(width):
            result_pixel = result.get_pixel(x, y)
            img_pixel = []
            # For every pixel, we compare pictures in images
            # to get the best pixel and renew it to the 'result'.
            for i in range(len(images)):
                single_img_pixel = images[i].get_pixel(x, y)
                img_pixel.append(single_img_pixel)
            # Embed the best pixel on the 'result'.
            best = get_best_pixel(img_pixel)
            result_pixel.red = best.red
            result_pixel.green = best.green
            result_pixel.blue = best.blue
    # return result
    ######## YOUR CODE ENDS HERE ###########
    # print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
