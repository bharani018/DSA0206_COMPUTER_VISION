import cv2

# Load the pre-trained classifier
face_cascade = cv2.CascadeClassifier("C:/Users/HP/OneDrive/Documents/COMPUTER_VISION/haarcascade_frontalface_alt.xml")

# Read the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/human.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the output image
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
