import numpy as np
import cv2


def color_image(image):

    try:
        # apply canny edge detection
        edges = cv2.Canny(image, 50, 150, apertureSize=3)

        # # Detect lines using Hough Line Transform
        lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

        # Create a copy of the original image to draw lines on
        image_with_lines = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Check if any lines are detected
        if lines is not None:
            for line in lines:
                rho, theta = line[0]
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))

                cv2.line(image_with_lines, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Find contours
        contours, _ = cv2.findContours(
            edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Fill each contour with a random color
        for contour in contours:
            color = np.random.randint(0, 255, size=(3,)).tolist()
            cv2.drawContours(image, [contour], -1, color, -1)
        return image
    except Exception as e:
        print(f"Error: {e}")
        return image
