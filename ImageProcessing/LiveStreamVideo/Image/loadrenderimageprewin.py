# loadrenderimageprewin.py
# Create a Pre-Window
# Load an image from file
# Render the image to an Image Window

import cv2

# Create a pre-Window
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

# Set the Filename
fileName = "imagedemo.png"

# Load the Image from file
image = cv2.imread(fileName)

# Show the image on screen
cv2.imshow("Image", image)

# Wait for a key press
cv2.waitKey(0)

# Close all open window
cv2.destroyAllWindows()