import numpy as np
import tensorflow as tf
from PIL import Image
from django.conf import settings
import os

# Intialize the global variables 
interpreter = None
input_details = None
output_details = None

# Class names for the plant disease
class_names = [
    'Apple___Black_rot', 'Apple___healthy', 'Apple___rust',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___healthy',
    'Corn_(maize)___Northern_Leaf_Blight', 'Potato___Early_blight',
    'Potato___healthy', 'Potato___Late_blight',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight',
    'Tomato___healthy', 'Tomato___Late_blight',
    'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus'
]
# Load the TFLite model and allocate tensors
def load_tflite_model():
    global interpreter, input_details, output_details
    model_path = os.path.join(settings.BASE_DIR, 'ml_model', 'plant_disease_model.tflite')
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

# Predict disease from a PIL image
def predict_disease(pil_image):
    global interpreter, input_details, output_details
# Check if the interpreter is already loaded
    if interpreter is None:
        load_tflite_model()

# Resize and preprocess the image
    image = pil_image.resize((128,128))
    image = np.array(image, dtype=np.float32)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0

# Ensure the input tensor is of the correct shape

    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])

    predicted_class = np.argmax(prediction, axis=1)[0]
    confidence = float(np.max(prediction)) * 100

    return class_names[predicted_class], confidence
