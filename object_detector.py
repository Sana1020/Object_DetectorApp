import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# Visualization Techniques
MARGIN = 10  # pixels
ROW_SIZE = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
TEXT_COLOR = (255, 0, 0)  # red

def visualize(image,detection_result) -> np.ndarray:
  """Draws bounding boxes on the input image and return it.
  Args:
    image: The input RGB image.
    detection_result: The list of all "Detection" entities to be visualize.
  Returns:
    Image with bounding boxes.
  """
  for detection in detection_result.detections:
    # Draw bounding_box
    bbox = detection.bounding_box
    start_point = bbox.origin_x, bbox.origin_y
    end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
    cv2.rectangle(image, start_point, end_point, TEXT_COLOR, 3)

    # Draw label and score
    category = detection.categories[0]
    category_name = category.category_name
    probability = round(category.score, 2)
    result_text = category_name + ' (' + str(probability) + ')'
    text_location = (MARGIN + bbox.origin_x,
                     MARGIN + ROW_SIZE + bbox.origin_y)
    cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                FONT_SIZE, TEXT_COLOR, FONT_THICKNESS)

  return image

# STEP 2: Create an ObjectDetector object.
base_options = python.BaseOptions(model_asset_path=r'C:\media_pipe\efficientdet_lite0.tflite')
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.5)
detector = vision.ObjectDetector.create_from_options(options)

##GUI-----
st.title("Object Detection App")
st.write("Upload an image to detect objects using MediaPipe's Object Detector.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    # first file
    #img.jpeg --> 255 216 224 0 16 ....... bytes xxxxxxxopencv
    
    #final input
    #bytearray(img.jpeg) --> array of bytes (255,216,224,0,16,...) Sequence of bytes
    #file =np.asarray(bytearray(img.jpeg),dtype=np.uint8) --> Numpy array of bytes array([255,216,224,0,16 ....]) 
    #image = cv2.imdecode(file,1) # 1 -->opencv
    #pixels
    #channels
    #high,width
    #format
    #uploaded_file --> RAW bytes array --> Image(Numpy array)
    file_bytes = np.asarray(bytearray(uploaded_file.read()),dtype=np.uint8)# Convert the uploaded file to a numpy array of bytes[0:255]
    image = cv2.imdecode(file_bytes,1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    st.image(image,'Uploaded Image')
    
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB,data = image)

    detection_result = detector.detect(mp_image)
    
    annotated_image = visualize(image, detection_result)
    st.image(annotated_image,'Detected Objects')