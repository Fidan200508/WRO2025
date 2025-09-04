import cv2
import numpy as np

class LaneDetector:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)

    def get_lane_error(self):
        ret, frame = self.cap.read()
        if not ret:
            return 0
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        # Simple center calculation
        h, w = edges.shape
        mid = w//2
        lane_center = np.mean(np.where(edges[h//2] > 0)[0])
        if np.isnan(lane_center):
            lane_center = mid
        error = mid - lane_center
        return error
