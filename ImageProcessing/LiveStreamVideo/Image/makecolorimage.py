# makecolorimage.py
# Make a Color image

import cv2
import numpy as np

# Image dimension
width = 255
height= 255

# Create a 3D color matrix
imageR = np.full((height, width, 3), 0.0)
imageG = np.full((height, width, 3), 0.0)
imageB = np.full((height, width, 3), 0.0)
imageW = np.full((height, width, 3), 0.0)
# Blue Image

# Print Array Dimensions
print(imageB.shape)

# Create a Gradient Blue matrix
for rowindex in range(imageB.shape[0]):
    colorvalue = 0
    for colindex in range(imageB.shape[1]):
        imageB[rowindex][colindex] = [colorvalue / 255.0, 0.0, 0.0]
        colorvalue += 1

# Print the Blue Image matrix
print(imageB)

# Create a Gradient Green matrix
for rowindex in range(imageG.shape[0]):
    colorvalue = 0
    for colindex in range(imageG.shape[1]):
        imageG[rowindex][colindex] = [0.0, colorvalue / 255.0, 0.0]
        colorvalue += 1

# Create a Gradient Red matrix
for rowindex in range(imageR.shape[0]):
    colorvalue = 0
    for colindex in range(imageR.shape[1]):
        imageR[rowindex][colindex] = [0.0, 0.0, colorvalue / 255.0]
        colorvalue += 1

# Create a Gradient White matrix
for rowindex in range(imageW.shape[0]):
    colorvalue = 0
    for colindex in range(imageW.shape[1]):
        pixelcolor = colorvalue / 255.0
        imageW[rowindex][colindex] = [pixelcolor, pixelcolor, pixelcolor]
        colorvalue += 1

# Show the images
cv2.imshow("Red Image", imageR)
cv2.imshow("Green Image", imageG)
cv2.imshow("Blue Image", imageB)
cv2.imshow("White Image", imageW)

# Wait for a key press
cv2.waitKey(0)

# Close all keys
cv2.destroyAllWindows()