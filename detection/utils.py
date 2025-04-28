#Creating a dummy function to stimulate disease prediction

import random

def dummy_predict(image_path):
     """
    Dummy function to simulate disease prediction.
    """
     labels =['Healthy','Bacterial Spot','Early Blight','Late Blight']
     # Simulate a random prediction
     predicted_label = random.choice(labels)
     confidence_score = round(random.uniform(70,99),2) #Random confidence score between 70 and 99
     return predicted_label, confidence_score