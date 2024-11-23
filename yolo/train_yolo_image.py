from ultralytics import YOLO

# Create a new YOLO model from scratch (suing yolo 8 nano)
model = YOLO("yolov8n.yaml")

# Load a pretrained YOLO model (recommended for training)
#model = YOLO("yolo11n.pt")

# Train the model using the 'config.yaml' dataset for 100 epochs
# epochs = rounds of training
# imgsz = resize image to set size
results = model.train(data="config.yaml", epochs=10000, imgsz=640, name='yolo_v8n_diep10k')

# Evaluate the model's performance on the validation set
#results = model.val()

# Perform object detection on an image using the model
#results = model("https://ultralytics.com/images/bus.jpg")

# Export the model to ONNX format
#success = model.export(format="onnx")

