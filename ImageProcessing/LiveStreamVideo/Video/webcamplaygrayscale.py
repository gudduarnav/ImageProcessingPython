# webcamplaygrayscale.py
# Open a Webcam or Default Video Capture Device
# Display the stream from the device
# Convert frame to grayscale and display

import cv2

# Create a Render Window
cv2.namedWindow("Color Video", cv2.WINDOW_NORMAL)
cv2.namedWindow("GrayScale Video", cv2.WINDOW_NORMAL)

# Set the Video Capture Device Index
vidIndex = 0

# Open the Video Capture Device
v = cv2.VideoCapture(vidIndex)

# Check if the file can be opened successfully
if(v.isOpened() == "False"):
    print("ERROR: Cannot open the Video Capture Device")
    quit()

print("SUCCESS: Video Capture Device opened")

# Read one frame from the file
while v.isOpened() == True:
    ret, image = v.read()
    
    # Check if the frame is successfully read
    if(ret == False):
        print("ERROR: Cannot read more video frame")
        break

    # Display the frame data
    cv2.imshow("Color Video", image)

    # Convert to grayscale
    imageBW = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the grasyscale Image 
    cv2.imshow("GrayScale Video", imageBW)

    # Wait for 10 ms for a user key press to exit
    if(cv2.waitKey(10) != -1):
        break

# Close the video file
v.release()

# Close all open window
cv2.destroyAllWindows()
