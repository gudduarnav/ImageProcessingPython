# loadrendergray.py
# Load an image from file
# Render the image to an Image Window
# Convert Image to Grayscale
# Render the Grayscale image

import cv2

# Create a pre-Window
cv2.namedWindow("Color Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Gray Image", cv2.WINDOW_NORMAL)

# Set the Filename
fileName = "imagedemo.png"

# Load the Color Image from file
image = cv2.imread(fileName)

# Show the color image on screen
cv2.imshow("Color Image", image)

# Convert image to Grayscale
imageBW = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show the Grayscale image on screen
cv2.imshow("Gray Image", imageBW)

# Wait for a key press
cv2.waitKey(0)

# Close all open window
cv2.destroyAllWindows()