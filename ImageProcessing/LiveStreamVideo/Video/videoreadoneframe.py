# videoreadoneframe.py
# Read the first frame from the Video file and display it as color image

import cv2

# Create a Render Window
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)

# Set the Video Filename
vidFile = "demo.mp4"

# Open the Video File
v = cv2.VideoCapture(vidFile)

# Check if the file can be opened successfully
if(v.isOpened() == False):
    print("ERROR: Video File cannot be opened")
    quit()

print("SUCCESS: Video File opened")

# Read one frame from the file
ret, image = v.read()

# Check if the frame is successfully read
if(ret == False):
    print("ERROR: Cannot read video frame")
    v.release()
    quit()

print("SUCCESS: A frame was read from file")

# Display the frame data
cv2.imshow("Video", image)

# Close the video file
v.release()

# Wait for a user keypress
cv2.waitKey(0)

# Close all open window
cv2.destroyAllWindows()
