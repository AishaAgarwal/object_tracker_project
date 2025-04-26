# main.py

import cv2
from src.detector import Detector
from src.tracker import Tracker

def main(video_path):
    detector = Detector()
    tracker = Tracker()

    seen_track_ids = set()
    previous_ids = set() 

    cap = cv2.VideoCapture(video_path)
    print("Video opened:", cap.isOpened())

    previous_ids = set()   # <-- added here!

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.detect(frame)
        tracks = tracker.update(detections, frame)

        current_ids = set()

        for track in tracks:
            track_id, x1, y1, x2, y2, class_id, conf = track
            current_ids.add(track_id)

            if track_id not in seen_track_ids:
                print(f"[+] New Object Detected: ID {track_id}")
                seen_track_ids.add(track_id)  # Mark as seen

            # Draw bounding box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f'ID: {track_id}', (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        if previous_ids:
            missing_objects = previous_ids - current_ids
            for obj in missing_objects:
                print(f"[-] Object Missing: ID {obj}")

        previous_ids = current_ids.copy()  # copy for next frame

        cv2.imshow("Real-Time Detection and Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "videos/person-bicycle-car-detection.mp4"
    main(video_path)
