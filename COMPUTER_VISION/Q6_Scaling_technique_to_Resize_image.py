import cv2
import os

# Path to the input image
image_path ="C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_1.png"

# Read the image
img = cv2.imread(image_path)

# Check if the image is loaded successfully
if img is None:
    print(f"Error: Unable to load the image at {image_path}")
    exit()

# Display the original image
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resize the image to a bigger size (scale factor > 1)
scale_factor_bigger = 2.0
new_height_bigger = int(img.shape[0] * scale_factor_bigger)
new_width_bigger = int(img.shape[1] * scale_factor_bigger)
resized_img_bigger = cv2.resize(img, (new_width_bigger, new_height_bigger))

# Display the resized image (bigger)
cv2.imshow('Resized Image (Bigger)', resized_img_bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resize the image to a smaller size (0 < scale factor < 1)
scale_factor_smaller = 0.5
new_height_smaller = int(img.shape[0] * scale_factor_smaller)
new_width_smaller = int(img.shape[1] * scale_factor_smaller)
resized_img_smaller = cv2.resize(img, (new_width_smaller, new_height_smaller))

# Display the resized image (smaller)
cv2.imshow('Resized Image (Smaller)', resized_img_smaller)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the resized images
output_folder = "C:/Users/HP/OneDrive/Pictures/computer_vision_images"
os.makedirs(output_folder, exist_ok=True)

output_path_bigger = os.path.join(output_folder, f"resized_bigger_{scale_factor_bigger}.jpg")
output_path_smaller = os.path.join(output_folder, f"resized_smaller_{scale_factor_smaller}.jpg")

cv2.imwrite(output_path_bigger, resized_img_bigger)
cv2.imwrite(output_path_smaller, resized_img_smaller)

print(f"Resized image (bigger) saved at: {output_path_bigger}")
print(f"Resized image (smaller) saved at: {output_path_smaller}")
