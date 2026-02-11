🖼️ Object Detection App using MediaPipe

🚀 Description

This is a simple web application built with Streamlit that allows you to upload an image and detect objects in it using MediaPipe's Object Detector (EfficientDet Lite0).
The app draws bounding boxes around detected objects with labels and confidence scores.

✨ Features

Upload JPG, JPEG, or PNG images.

Detect multiple objects in an image.

Visualize results with bounding boxes and labels.

Works entirely in the browser via Streamlit.

📦 Requirements

Install the required packages:

pip install streamlit opencv-python mediapipe numpy

Also, download the EfficientDet Lite0 model (efficientdet_lite0.tflite) from MediaPipe and place it in your project folder. Make sure the path in app.py matches where you saved it.

⚡ How to Run

streamlit run app.py

Upload an image and see the detected objects.

🗂️ Project Structure
├── app.py                     # Main Streamlit application
├── efficientdet_lite0.tflite  # MediaPipe Object Detection model
└── README.md                  # Project description and instructions
