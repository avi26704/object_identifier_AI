from ultralytics import YOLO
model = YOLO('yolov8n.pt')
cap=model.predict(source='0',show=True)