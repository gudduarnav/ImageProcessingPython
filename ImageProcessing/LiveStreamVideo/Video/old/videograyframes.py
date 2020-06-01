# Read a Video stream from file and stream it on screen in Grayscale format

import cv2

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
    ret, frame = v.read()
    
    # Check if the frame is successfully read
    if(ret == False):
        print("ERROR: Cannot read more video frame")
        break

    # Convert to grayscale
    gframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the frame data
    cv2.imshow("Video Frame", gframe)

    # Wait for 25 ms for a user key press to exit
    if(cv2.waitKey(25) != -1):
        break

# Close the video file
v.release()

# Close all open window
cv2.destroyAllWindows()
