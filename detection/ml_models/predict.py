import numpy as np
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
from django.conf import settings
import os

model = None  # global model cache

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
    global model
    model_path = os.path.join(settings.BASE_DIR, 'ml_model', 'plant_disease_model.h5')
    if model is None:
        try:
            model = load_model(model_path)
        except OSError:
            print(f"Model file not found at {model_path}. Returning dummy result.")
            return "Model Not Found", 0.0

    image = pil_image.resize((128,128))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0

    prediction = model(image, training=False).numpy()
    predicted_class = np.argmax(prediction, axis=1)[0]

    return class_names[predicted_class], float(np.max(prediction)) * 100
