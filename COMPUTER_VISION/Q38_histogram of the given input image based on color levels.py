import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input image
image_path = "C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg"
image = cv2.imread(image_path)

# Convert the image from BGR to RGB (OpenCV uses BGR by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Calculate the histogram for each color channel
hist_blue = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_green = cv2.calcHist([image], [1], None, [256], [0, 256])
hist_red = cv2.calcHist([image], [2], None, [256], [0, 256])

# Plot the histograms
plt.figure(figsize=(12, 6))

plt.subplot(131)
plt.plot(hist_blue, color='blue')
plt.title('Blue Channel Histogram')

plt.subplot(132)
plt.plot(hist_green, color='green')
plt.title('Green Channel Histogram')

plt.subplot(133)
plt.plot(hist_red, color='red')
plt.title('Red Channel Histogram')

plt.tight_layout()
plt.show()

