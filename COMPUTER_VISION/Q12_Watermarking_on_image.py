import cv2
import numpy as np

# Read the input image and the watermark image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg")
watermark = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/watermark_ime.jpg", cv2.IMREAD_UNCHANGED)

# Resize the images to the same size
img = cv2.resize(img, (watermark.shape[1], watermark.shape[0]))

# Define the points for the input image and the corresponding points for the output image
pts1 = np.float32([[0, 0], [watermark.shape[1], 0], [0, watermark.shape[0]], [watermark.shape[1], watermark.shape[0]]])
pts2 = np.float32([[100, 100], [100+watermark.shape[1], 100], [100, 100+watermark.shape[0]], [100+watermark.shape[1], 100+watermark.shape[0]]])

# Compute the perspective transform matrix M using cv2.getPerspectiveTransform(pts1, pts2) function
M = cv2.getPerspectiveTransform(pts1, pts2)

# Transform the watermark image using cv2.warpPerspective() method
watermark_transformed = cv2.warpPerspective(watermark, M, (img.shape[1], img.shape[0]))

# Define the alpha blending factor
alpha = 0.5

# Apply the watermark to the input image using cv2.addWeighted() function
result = cv2.addWeighted(img, 1-alpha, watermark_transformed, alpha, 0)

# Display the watermarked image
cv2.imshow("Watermarked Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
