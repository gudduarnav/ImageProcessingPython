# loadresizerenderimage.py
# Load an image from file
# Resize Image and Render the resized image
import cv2

# Create a pre-Window
cv2.namedWindow("Original", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Half-Size", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Double-Size", cv2.WINDOW_AUTOSIZE)

# Set the Filename
fileName = "imagedemo.png"

# Load the Color Image from file
originalImage = cv2.imread(fileName)

# Retrieve Width and Height of Original Image
originalHeight = originalImage.shape[0]
originalWidth  = originalImage.shape[1]

# Show the color image on screen
cv2.imshow("Original", originalImage)


# Resize Image to Half Size

# Obtain new dimension
halfScaleHeight = 0.5
halfScaleWidth  = 0.5
halfHeight = int(originalHeight * halfScaleHeight)
halfWidth  = int(originalWidth  * halfScaleWidth)

# Resize the image 
halfImage = cv2.resize(originalImage, (halfWidth,halfHeight), cv2.INTER_AREA)

# Display the image
cv2.imshow("Half-Size", halfImage)

# Resize Image to Double Size

# Obtain new dimension
doubleScaleHeight = 2.0
doubleScaleWidth  = 2.0
doubleHeight = int(originalHeight * doubleScaleHeight)
doubleWidth  = int(originalWidth  * doubleScaleWidth)

# Resize the image
doubleImage = cv2.resize(originalImage, (doubleWidth, doubleHeight), cv2.INTER_CUBIC)

# Display the image
cv2.imshow("Double-Size", doubleImage)



# Wait for a key press
cv2.waitKey(0)

# Close all open window
cv2.destroyAllWindows()