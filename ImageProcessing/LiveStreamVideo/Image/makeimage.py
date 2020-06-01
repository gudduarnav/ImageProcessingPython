# makeimage.py
# Make a Gray scale image

import cv2
import numpy as np

# Image dimension
width = 255
height= 255

# Create a 2D array
image = np.full((height, width), 0.0)

# Print Array Dimensions
print(image.shape)

# Create a Gradient Image
for rowindex in range(image.shape[0]):
    colorvalue = 0
    for colindex in range(image.shape[1]):
        image[rowindex][colindex] = colorvalue / 255.0
        colorvalue += 1

# Print the Image matrix
print(image)

# Show the image
cv2.imshow("Image", image)

# Wait for a key press
cv2.waitKey(0)

# Close all keys
cv2.destroyAllWindows()