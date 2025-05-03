#Creating a dummy function to stimulate disease prediction

import random

def dummy_predict(image_url):
    print(f"Received image URL: {image_url}")  # Debugging

    # Simulate random predictions
    predictions = ["Healthy", "Unhealthy", "Diseased"]
    prediction = random.choice(predictions)
    confidence = round(random.uniform(70, 100), 2)  # Random confidence between 70% and 100%

    print(f"Prediction: {prediction}, Confidence: {confidence}")  # Debugging
    return prediction, confidence