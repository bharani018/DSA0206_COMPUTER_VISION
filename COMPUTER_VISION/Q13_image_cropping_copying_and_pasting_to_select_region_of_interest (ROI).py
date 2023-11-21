import cv2

# Read the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg")

# Define the region of interest (ROI) using NumPy slicing
x, y, width, height = 100, 100, 300, 400
roi = img[y:y+height, x:x+width]

# Display the cropped image
cv2.imshow("Cropped Image", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
