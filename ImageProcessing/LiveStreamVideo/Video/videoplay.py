# videoplay.py
# Stream a Color Video stream from video source file

import cv2

# Create a Render Window
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)

# Set the Video Filename
vidFile = "demo.mp4"

# Open the Video File
v = cv2.VideoCapture(vidFile)

# Check if the file can be opened successfully
if(v.isOpened() == "False"):
    print("ERROR: Cannot open the Video File")
    quit()

print("SUCCESS: Video File opened")

# Read one frame from the file
while v.isOpened() == True:
    ret, image = v.read()
    
    # Check if the frame is successfully read
    if(ret == False):
        print("ERROR: Cannot read more video frame")
        break

    # Display the frame data
    cv2.imshow("Video", image)

    # Wait for 25 ms for a user key press to exit
    if(cv2.waitKey(25) != -1):
        break

# Close the video file
v.release()

# Close all open window
cv2.destroyAllWindows()
