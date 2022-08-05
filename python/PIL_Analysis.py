Python Pillow 

PIL - (Python Image Library)

Digital Image processing means processing the image digitally with the help of a computer. Using image processing we can perform operations like enhancing the image, blurring the image, extracting text from images, and many more operations. There are various ways to process images digitally. Here we will discuss the Pillow module of Python.


# Installation
pip install pillow

# Opening and Displaying the image
from PIL import Image

# Location of the image
img = Image.open("imagename")

img.show()


# Getting information about the opened image
# Getting the Size, and format of the Image

# size of the image
print(img.size)
 
# format of the image
print(img.format)


# Getting Color mode of the image:
1	1-bit pixels, black and white
L	8-bit pixels, Greyscale
P	8-bit pixels, mapped to any other mode using a color palette
RGB	3×8-bit pixels, true color
RGBA	4×8-bit pixels, true color with transparency mask

print(img.mode)


# Rotating the Image
img = img.rotate(180)

# Transpose image (mirror effect)
img = img.transpose(method = Image.TRANSPOSE)

# Flipping the Image
# FLIP_TOP_BOTTOM – returns an original image flipped Vertically
# FLIP_LEFT_RIGHT – returns an original image flipped Horizontally

img = img.transpose(method = Image.FLIP_TOP_BOTTOM)
img = img.transpose(method = Image.FLIP_Left_Right)

# Saving the Image
img.save('imagename')