
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