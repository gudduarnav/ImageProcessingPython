# Live stream a Colored video from Webcam or default Video Capture device

import cv2

# Open the default Video Capture device (or WebCam)
v = cv2.VideoCapture(0)

# Check if the file can be opened successfully
if(v.isOpened() == "False"):
    print("ERROR: Cannot open the Video File")
    quit()

print("SUCCESS: Video File opened")

# Read one frame from the file
while v.isOpened() == True:
    ret, frame = v.read()
    
    # Check if the frame is successfully read
    if(ret == False):
        print("ERROR: Cannot read more video frame")
        break

    # Display the frame data
    cv2.imshow("Video Frame", frame)

    # Wait for 25 ms for a user key press to exit
    if(cv2.waitKey(25) != -1):
        break

# Close the video file
v.release()

# Close all open window
cv2.destroyAllWindows()
