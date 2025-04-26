# src/tracker.py

from deep_sort_realtime.deepsort_tracker import DeepSort

class Tracker:
    def __init__(self, max_age=30, n_init=3):
        # Initialize Deep SORT
        self.tracker = DeepSort(max_age=max_age, n_init=n_init)

    def update(self, detections, frame):
        """
        Takes detections and frame, returns tracked objects.
        
        detections format: [[x1, y1, x2, y2, confidence, class_id], ...]
        
        returns: list of tracked objects -> 
        [ [ID, x1, y1, x2, y2, class_id, confidence], ... ]
        """
        det_list = []
        for det in detections:
            x1, y1, x2, y2, conf, class_id = det
            w = x2 - x1
            h = y2 - y1
            det_list.append(([x1, y1, w, h], conf, class_id))

        tracks = self.tracker.update_tracks(det_list, frame=frame)
        output = []
        for track in tracks:
            if not track.is_confirmed():
                continue
            track_id = track.track_id
            ltrb = track.to_ltrb()  # left, top, right, bottom
            class_id = track.det_class
            conf = track.det_conf
            output.append([track_id, *ltrb, class_id, conf])

        return output
