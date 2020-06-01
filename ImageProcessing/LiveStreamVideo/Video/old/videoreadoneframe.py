# Read the first frame from the Video file and display it as color image

import cv2

# Set the Video Filename
vidFile = "demo.mp4"

# Open the Video File
v = cv2.VideoCapture(vidFile)

# Check if the file can be opened successfully
if(v.isOpened() == False):
    print("ERROR: Cannot open the Video File")
    quit()

print("SUCCESS: Video File opened")

# Read one frame from the file
ret, frame = v.read()

# Check if the frame is successfully read
if(ret == False):
    print("ERROR: Cannot read video frame")
    v.release()
    quit()

# Display the frame data
cv2.imshow("Video Frame", frame)

# Close the video file
v.release()

# Wait for a user keypress
cv2.waitKey(0)

# Close all open window
cv2.destroyAllWindows()
