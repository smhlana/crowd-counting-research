# CIFAR-10 CNN Classifier

A web-based image classification application built with Flask and PyTorch that uses a custom-trained Convolutional Neural Network (CNN) to classify images into one of 10 CIFAR-10 categories.

**Classification Categories**
Plane, Car, Bird, Cat, Deer, Dog, Frog, Horse. Ship, Truck

## Project Overview

This project implements a **custom CNN architecture trained from scratch** on the CIFAR-10 dataset, specifically for the 10 CIFAR-10 classes.

## Model Architecture

**Custom CNN Structure:**
- **Convolutional Layers**: 2 Conv2D layers (3→6→16 channels)
- **Pooling**: MaxPooling2D layers for downsampling
- **Fully Connected**: 3 Dense layers (400→120→84→10)
- **Activation**: ReLU activation functions
- **Output**: 10 classes with softmax probability

**Training Details:**
- **Dataset**: CIFAR-10 (50,000 training images, 10,000 test images)
- **Input Size**: 32×32×3 RGB images
- **Framework**: PyTorch
- **Trained**: Custom training loop with data augmentation

## Features

- **Custom CNN Model**: Built and trained from scratch (not pre-trained)
- **Real-time Classification**: Upload and classify images instantly
- **Confidence Visualization**: Color-coded confidence levels
  - 🟢 **Green**: High confidence (≥70%)
  - 🟠 **Orange**: Medium confidence (40-70%)
  - 🔴 **Red**: Low confidence (<40%)

## Prerequisites

- **Python 3.7+**
- **PyTorch** (CPU version is sufficient for inference)
- **Flask** for the web application
- **Pillow** for image processing

## Installation

### 1. Install Dependencies

```bash
# Navigate to project directory
cd crowd-counting-experiments/experiments/cifar10-cnn-classifier

# Install required packages
pip install -r requirements.txt
```

## Running the Application

```bash
# Run the Flask application
python app.py
```

**Access the application:**
- Open browser: `http://localhost:3000`
- Upload an image
- Get instant classification results!

## References & Learning Resources

This project was built following concepts from these educational resources:

### **Course Reference**
- **[Computer Vision & Deep Learning with Python](https://www.udemy.com/course/computervision-deeplearning-with-python/)** - Udemy Course
  - Comprehensive course covering computer vision fundamentals and deep learning implementation

### **Tutorial Reference**  
- **[Deploy Machine Learning Models using Flask](https://www.youtube.com/watch?v=0nr6TPKlrN0&t=2s)** - YouTube Tutorial
  - Hands on tutorial on how to deploy an ML model with Python using Flask.

## License

This project is for educational purposes as part of crowd counting and computer vision research experiments.
