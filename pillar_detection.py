import cv2
import numpy as np

class PillarDetector:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)

    def detect_pillars(self):
        ret, frame = self.cap.read()
        if not ret:
            return {"red": [], "green": []}
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Red mask
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        # Green mask
        lower_green = np.array([40, 40, 40])
        upper_green = np.array([80, 255, 255])
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        red_centers = np.column_stack(np.where(mask_red > 0))
        green_centers = np.column_stack(np.where(mask_green > 0))
        return {"red": red_centers.tolist(), "green": green_centers.tolist()}
