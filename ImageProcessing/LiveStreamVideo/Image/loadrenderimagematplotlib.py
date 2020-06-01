# loadrenderimagematplotlib.py
# Read Image using OpenCV
# Display Image using MATPLOTLIB

import cv2
import matplotlib.pyplot as plt


# Set Path to Image File
imgFile = "imagedemo.png"

# Load the Image
image = cv2.imread(imgFile)          

# Render the image using OpenCV
cv2.imshow("OpenCV Image Viewer", image)

# Covert BGR to RGB color-space 
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the Image using MATPLOTLIB pyplot
f1 = plt.figure()
f1.canvas.set_window_title("MATPLOTLIB Image Viewer")
ax = f1.add_axes([0,0,1,1])
ax.imshow(imageRGB, cmap="jet", interpolation="bicubic")

plt.show()

cv2.destroyAllWindows()
