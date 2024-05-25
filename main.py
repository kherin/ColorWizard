import cv2
import numpy as np

# load the image
image_path = "img/coloring_book.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print(f"Failed to load image: {image_path}")
else:
    print(f"Image loaded successfully: {image_path}")

# apply canny edge detection
edges = cv2.Canny(image, 50, 150, apertureSize=3)

# window configuration
window_name = 'Color Wizard'

# Invert the edges image so that edges are black (255) and background is white (0)
final_image = cv2.bitwise_not(edges)

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 800)

# display the edges
cv2.imshow(window_name, final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
