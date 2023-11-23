import cv2

# Load the pre-trained classifiers for face and smile detection
face_cascade = cv2.CascadeClassifier("C:/Users/HP/OneDrive/Documents/COMPUTER_VISION/haarcascade_frontalface_alt.xml")
smile_cascade = cv2.CascadeClassifier("C:/Users/HP/OneDrive/Documents/COMPUTER_VISION/haarcascade_smile.xml")

# Read the input image
image = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/human.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Detect smiles within each detected face
for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)

# Display the image with smile detection
cv2.imshow('Smile Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
