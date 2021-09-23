# self_learning-image_processing
Reference to Stanford University’s assignment CS106AP: Programming Methodologies in Python and CS106B: Programming Abstractions as practice, focusing topic:  image processing
## Projects Source Codes:
* [01_photoshop](https://github.com/An022/self_learning-image_processing/edit/main/01_photoshop/stanCodoshop.py)\
  Exacuating basic processing imagine building a mini photoshop, which compares a series of pictures,\
  then renew the pixel to erase the pedestrian in the photo by returning the color distance between pixels and mean RGB value.

  ```
  We compare a series of pictures, then renew the pixel to erase the pedestrian in the photo.
  Returns the color distance between pixel and mean RGB value
  
  pre-condition:
  Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images
  post-condition: 
  Returns:
        dist (int): color distance between red, green, and blue pixel values
  ```
* [02_mirror_lake](https://github.com/An022/self_learning-image_processing/blob/main/02_mirror_lake/mirror_lake.py)\
  This file reads in mt-rainier.jpg and makes a new image that creates a mirror lake vibe by placing an inverse image of mt-rainier.jpg below the original one.
  
  ```
  Use this program can help user find the homology in a DNA sequence.
  
  pre-condition: 
  :param filename: str, the file path of the original colored image.
  post-condition: 
  :return: SimpleImage, With doubling the original height, the new imagine size will be twice as the original one
  and combined by the original image and a mirror image.
  ```
* [03_blur_and_shrink]
  * [blur](https://github.com/An022/self_learning-image_processing/blob/main/03_blur_and_shrink/blur.py)\
    “Blur” shows the original image first, and then compares to its blurred image.\
    The blur algorithm uses the average RGB values of a pixel's nearest neighbors.

    ```
    This file shows the original image first, smiley-face.png, and then compare to its blurred image. 

    pre-condition: 
    :param img: str, the file path of the original background image.
    post-condition: 
    :return:SimpleImage, the blurred version of the original image.
    ```
  * [shrink](https://github.com/An022/self_learning-image_processing/blob/main/03_blur_and_shrink/shrink.py)
    "Shirnk" produces a image with 1/2 width and 1/2 height of the original imagine.

    ```
    Create a new "out" image half the width and height of the original.
    Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,and likewise in the y direction.

    pre-condition: 
    :param filename: str, the file path of the original colored image.
    post-condition:
    :return img: SimpleImage, the shrink imagine with 1/2 width and 1/2 height of original img.
    ```
* [04_green_screen](https://github.com/An022/self_learning-image_processing/blob/main/04_green_screen/green_screen.py)\
  Greenscreen creates a new image that removes the background and replaces the green pixels in it.

  ```
  This file creates a new image that uses MillenniumFalcon.png as background
  and replace the green pixels in "ReyGreenScreen.png".
  
  pre-condition:
  :param background_img: str, the file path of the original background image.
  :param figure_img: str, the file path of the original figure image.
  post-condition:
  :return: Replace the green background in figure imagine into the background imagine.
  ```
* [05_fire_alarm](https://github.com/An022/self_learning-image_processing/blob/main/05_fire_alarm/fire_alarm.py)\
  The program will check the imagine to see if there are any fire happened in the forest.\
  If any area has a highly chance of having forest fire, the imagine will reflect the color with red\
  On the contracts, those safe area's original color will be turned into gray scale.\
  Fire alarm contains a method called highlight_fires which detects the pixels that are recognized as fire and highlights them for better observation.

  ```
  Highlighting fire area with full red while other safe areas' color will be turned into grayscale.
  
  pre-condition:
  :param filename: str, the file path of the original colored image.
  post-condition:
  :return:The image with the fire area will be highlighted by full red 
          while other safe areas' color will be turned into gray scale.
  ```
* [06_green_screen](https://github.com/An022/self_learning-image_processing/blob/main/06_find_willy/find_willy.py)\
  Duplicating multiple starwar picture and combining my own picture together to create a new version game of "find willy".

  ```
  Combine the figure and background, then make whole new image left only two color: black and white.
  Then make a maze with original background to hide the figure.
  Let's play "find Willy" !
  
  pre-condition:
  :param background_img: str, the file path of the original background image.
  :param figure_img: str, the file path of the original figure image.
  post-condition:
  :return: Replace the green background in figure imagine into the background imagine.
  ```
  
