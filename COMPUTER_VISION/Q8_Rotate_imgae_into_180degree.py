import cv2

# Load the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg")

# Rotate the image by 180 degrees clockwise
img_rotated = cv2.rotate(img, cv2.ROTATE_180)

# Display the rotated image
cv2.imshow("Rotated Image", img_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
