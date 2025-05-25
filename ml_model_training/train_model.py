import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam 


#define paths
dataset_path ='dataset/PlantVillage'
img_height, img_width = 128, 128
batch_size = 32
epochs = 10

#data augmentation
datagen = ImageDataGenerator(rescale=1./255,validation_split=0.2)

train_data = datagen.flow_from_directory(
    dataset_path,
    target_size = (img_height, img_width),
    batch_size = batch_size,
    class_mode = 'categorical',
    subset = 'training'
)

val_data = datagen.flow_from_directory(
    dataset_path,
    target_size = (img_height, img_width),
    batch_size = batch_size,
    class_mode = 'categorical',
    subset = 'validation'
)

#CNN model

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(img_height, img_width, 3)),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(len(train_data.class_indices), activation='softmax')
])

#Compile the model
model.compile(optimizer=Adam(),loss='categorical_crossentropy',metrics=['accuracy'])

#Train the model
history = model.fit(train_data, validation_data=val_data, epochs=epochs)


#Save the model
model.save('model/plant_disease_model.h5')

print("Model training complete and saved")
