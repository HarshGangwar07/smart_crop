import numpy as np
from PIL import Image
from django.conf import settings
import os
import tensorflow as tf

# Path to the .tflite model
model_path = os.path.join(settings.BASE_DIR, 'ml_model', 'plant_disease_model.tflite')

# Load the TFLite model and allocate tensors only once
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input and output tensor details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Class names used for prediction
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

def predict_disease(pil_image):
    # Preprocess the image
    image = pil_image.resize((128, 128))
    image = np.array(image) / 255.0
    image = np.expand_dims(image.astype(np.float32), axis=0)

    # Set the input tensor
    interpreter.set_tensor(input_details[0]['index'], image)

    # Run inference
    interpreter.invoke()

    # Get the output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]

    # Get predicted class and confidence
    predicted_class = np.argmax(output_data)
    confidence = float(output_data[predicted_class]) * 100

    return class_names[predicted_class], confidence
