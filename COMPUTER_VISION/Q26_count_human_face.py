import cv2

# Load the pre-trained Haar Cascade face detector
face_cascade = cv2.CascadeClassifier("C:/Users/HP/OneDrive/Documents/COMPUTER_VISION/haarcascade_frontalface_alt.xml")

# Read the input image
image_path = "C:/Users/HP/OneDrive/Pictures/computer_vision_images/people.jpg"
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image with detected faces
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the number of detected faces
print(f'Number of faces detected: {len(faces)}')
