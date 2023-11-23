import cv2

# Load the pre-trained classifier
plate_cascade = cv2.CascadeClassifier("C:/Users/HP/OneDrive/Documents/COMPUTER_VISION/haarcascade_license_plate_rus_16stages.xml")

# Read the input video
cap = cv2.VideoCapture("C:/Users/HP/OneDrive/Pictures/computer_vision_images/vehicle.mp4")

# Loop through each frame of the video
while True:
    # Read the frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect license plates in the frame
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected license plates
    for (x, y, w, h) in plates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Display the output video
    cv2.imshow('License Plate Detection', frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
