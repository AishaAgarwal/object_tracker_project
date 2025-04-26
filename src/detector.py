# src/detector.py

from ultralytics import YOLO

class Detector:
    def __init__(self, model_path="yolov8n.pt", conf_threshold=0.4):
        # Load the YOLOv8 model
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold

    def detect(self, frame):
        """
        Takes a frame and returns detections: 
        list of [x1, y1, x2, y2, confidence, class_id]
        """
        results = self.model.predict(frame, verbose=False)[0]
        detections = []

        for box in results.boxes:
            if box.conf.item() >= self.conf_threshold:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                conf = box.conf.item()
                class_id = int(box.cls.item())
                detections.append([x1, y1, x2, y2, conf, class_id])

        return detections
