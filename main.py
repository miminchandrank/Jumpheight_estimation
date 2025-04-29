# main.py

import cv2
from Pose_module import PoseDetector
from calibration_module import Calibration
from jump_module import JumpTracker
from utils import find_point

# Config
REAL_PERSON_HEIGHT_METERS = 1.75  # Example: 1.75 meters

cap = cv2.VideoCapture(0)  # Webcam (or use video file)

pose_detector = PoseDetector()
calibration = Calibration(real_height_meters=REAL_PERSON_HEIGHT_METERS)
jump_tracker = JumpTracker()

calibrated = False

while True:
    success, img = cap.read()
    if not success:
        break

    img = pose_detector.find_pose(img)
    landmarks = pose_detector.get_landmarks(img)

    if landmarks:
        head = find_point(landmarks, 0)  # Nose ID = 0, better use 0 or 1
        left_foot = find_point(landmarks, 27)  # Left ankle
        right_foot = find_point(landmarks, 28)  # Right ankle

        hip = find_point(landmarks, 24)  # Right hip

        if head and left_foot and right_foot and hip:
            foot_y = max(left_foot[1], right_foot[1])

            # Calibrate once when standing
            if not calibrated:
                calibration.set_pixel_height(head[1], foot_y)
                calibrated = True
                print("Calibration done based on body height.")

            # Track jump
            jump_tracker.update(hip[1])

            # Convert pixels to meters
            pixel_jump = jump_tracker.get_max_jump()
            real_jump_meters = calibration.pixel_to_meters(pixel_jump)

            # Display
            cv2.putText(img, f"Jump Height: {real_jump_meters:.2f} meters", (30, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Jump Height Estimation", img)

    key = cv2.waitKey(1)
    if key == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
