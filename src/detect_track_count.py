import cv2
from ultralytics import YOLO
from tracker import Tracker

# Load YOLO model
model = YOLO("models/yolov8n.pt")

# Load video
cap = cv2.VideoCapture("input/traffic.mp4")

if not cap.isOpened():
    print("ERROR: Cannot open video")
    exit()
else:
    print("Video opened successfully")

tracker = Tracker()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    detections = []

    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        classes = result.boxes.cls.cpu().numpy()

        for box, cls in zip(boxes, classes):

            # Only detect vehicles (car=2, motorcycle=3, bus=5, truck=7 in COCO)
            if int(cls) in [2, 3, 5, 7]:
                x1, y1, x2, y2 = box
                detections.append([x1, y1, x2, y2])

    # Update tracker
    tracker.update(detections)

    # Draw tracked boxes
    for track in tracker.tracks:
        x1, y1, x2, y2, track_id = track
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
        cv2.putText(frame, str(track_id), (int(x1), int(y1)-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.imshow("Vehicle Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()