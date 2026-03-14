
## Image Classification 

A Deep Learning based image classification system that detects the type of flower from an uploaded image.

The project trains a Convolutional Neural Network (CNN) using TensorFlow to classify flower images into different categories.

The application also includes an interactive web interface built with Streamlit, where users can upload a flower image and instantly see the predicted flower type.

---
## Project Overview

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

**Example:**

<img width="443" height="272" alt="Image" src="https://github.com/user-attachments/assets/c125a72b-faf9-44f7-a2be-d95c0ee61bef" />

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

Click the video below to watch the demo:

https://github.com/user-attachments/assets/60320976-8c38-4a7f-80a6-e7cb46566c49


---
# ⚙️ Installation and Setup

## 1. Download the repository

It will be downloaded in Zip file so you have to **Extract** the files. A direct link to the repository is available below or click on **Download Repository** and you will be redirected to the repository.

```
https://github.com/rohitvirdi5rv-crypto/Image-Classification-Project.git
```

[Download Repository](https://github.com/rohitvirdi5rv-crypto/Image-Classification-Project.git)

---
## 2. Create a virtual environment

```
python -m venv venv
```

**Activate it on Windows:**

```
venv\Scripts\activate
```

---
## 5. Run the Streamlit app

```
streamlit run app.py
```

The application will open in your browser.

---
## Live Project

The application has been successfully deployed.  
You can check out the **Image Flower Classifier** using the link below:

[Click here to open the deployed application](https://image-classification-project-dbnnidvg68ep6zmelefdcj.streamlit.app/)

---
## 🔮 Future Improvements

Possible improvements for this project:

* Add more flower categories
* Improve accuracy using data augmentation
* Use transfer learning models (ResNet, MobileNet)
* Deploy the application online
* Add prediction confidence score

---