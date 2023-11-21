import cv2
path="C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow(window_name, image)
cv2.waitKey(0)
