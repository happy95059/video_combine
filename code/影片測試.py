import cv2
import time
# Open a video file
cap = cv2.VideoCapture('../data/video_trans.avi')

# Check if video file opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Read the video file frame by frame
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, display it
    if ret:
        cv2.imshow('frame', frame)  
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop if end of file is reached
    else:
        break
    time.sleep(0.05)
# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()