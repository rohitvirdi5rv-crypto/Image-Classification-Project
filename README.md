
## Image Classification 

A Deep Learning based image classification system that detects the type of flower from an uploaded image.

The project trains a Convolutional Neural Network (CNN) using TensorFlow to classify flower images into different categories.

The application also includes an interactive web interface built with Streamlit, where users can upload a flower image and instantly see the predicted flower type.

---
## Project Overview

Image classification is one of the most common applications of deep learning in computer vision.

This project builds a CNN-based model that automatically identifies different types of flowers from images.

The system works in three main stages:

* Dataset preparation – Load and organize flower image data

* Model training – Train a CNN model using TensorFlow

* Prediction – Classify uploaded images through a Streamlit web application

---
# 🧠 How the Model Works

## 1. Dataset

The model is trained using the TensorFlow Flower Photos Dataset, which contains images of different flower categories.

**Flower classes used in the project:**

* Daisy
* Dandelion
* Rose
* Sunflower
* Tulip

**Dataset is automatically downloaded from:**

```
https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz
```

---
## 2. Data Preprocessing

Before training the model, the images go through several preprocessing steps:

* Resize images to 180 × 180 pixels
* Normalize pixel values using Rescaling
* Shuffle training data for better learning
* Split dataset into training and validation sets

**Dataset split:**

* 80% Training Data
* 20% Validation Data

---
## 3. Model Architecture

The project uses a Convolutional Neural Network (CNN) built using TensorFlow/Keras.

**The architecture includes:**

* Image Rescaling Layer
* Conv2D Layers for feature extraction
* MaxPooling Layers for dimensionality reduction
* Flatten Layer
* Dense Hidden Layer
* Output Layer for classification

**Example architecture:**

![App Screenshot](https://github.com/rohitvirdi5rv-crypto/Image-Classification-Project/blob/3498f1671ce74148d1c4d7215fe1223f4499d6cb/Project%20Related%20Screenshots/Screenshot%202026-03-13%20232136.png)

---
## 4. Model Training

The model is trained using:

* **Optimizer:** Adam
* **Loss Function:** Sparse Categorical Crossentropy
* **Epochs:** 20
* **Batch Size:** 32

During training, the model learns patterns such as:

* Petal shapes
* Flower colors
* Texture and structure

---


## 5. Model Saving

After training, the model is saved for later use.

**Saved model file:**

```
Image_Classification_Model.hdf5
```
This file is used by the Streamlit application to make predictions on new images.

---
## 🌐 Web Application

The project includes a user-friendly web interface built with Streamlit.

**Features of the App:**

* Upload a flower image
* Run the trained CNN model
* Instantly get the predicted flower category

---
## 🎥 Application Demo



---
