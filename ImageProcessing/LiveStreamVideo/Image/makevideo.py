# makevideo.py
# Generate a video like color image in real time

import cv2
import numpy as np

# Video image settings
width = 255             # pixels
height = 255            # pixels
framerate = 10          # frames per seconds
timedelay = 1000 // framerate   # time delay between frames

# Allocate the image
image = np.full((height, width, 3), 0.0)

# Color Value
colorrgb = 0

# Animation Loop
while True:
    # Generate the image

    # Paint the pixel with the color
    for rowindex in range(image.shape[0]):
        for colindex in range(image.shape[1]):
            # Update the color
            colorrgb += 1
            colorrgb = colorrgb % (256*256*256)

            # Extract the individual color
            colorR = colorrgb % 256
            colorG = (colorrgb//256) % 256
            colorB = (colorrgb//(256*256)) % 256

            # Update the color value
            image[rowindex][colindex][0] = colorB / 255.0
            image[rowindex][colindex][1] = colorG / 255.0
            image[rowindex][colindex][2] = colorR / 255.0

    # Show the Frame
    cv2.imshow("Video", image)

    # Exit from animated loop when the user presses a key
    if cv2.waitKey(timedelay) != -1:
        break

# Close the open window
cv2.destroyAllWindows()

