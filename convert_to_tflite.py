import tensorflow as tf
import os

#Defining the path to my .h5 model
model_path = os.path.join('ml_model','plant_disease_model.h5')
output_path = os.path.join('ml_model', 'plant_disease_model.tflite')

#Load the model
model = tf.keras.models.load_model(model_path)

#Convert the model to TFLite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)

#Optimize the model for size
converter.optimizations = [tf.lite.Optimize.DEFAULT]

#Convert the model
tflite_model = converter.convert()

#Save the converted model to a file
with open(output_path, 'wb') as f:
    f.write(tflite_model)

print(f"TFLite model saved to {output_path}")