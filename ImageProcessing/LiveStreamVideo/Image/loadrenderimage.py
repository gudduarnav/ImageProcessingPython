# loadrenderimage.py
# Load an image from file
# Render the image to an Image Window

import cv2

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