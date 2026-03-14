# Flask Image Classifier

A web-based image classification application built with Flask and TensorFlow that uses the pre-trained VGG16 model to classify uploaded images.

## Features

- **Web Interface**: Simple and intuitive web interface for image upload
- **Image Classification**: Uses VGG16 pre-trained model for accurate image classification
- **Confidence Colour Coding**: Visual feedback based on prediction confidence levels:
  - 🟢 **Green**: High confidence (≥70%)
  - 🟠 **Orange**: Medium confidence (40-70%)
  - 🔴 **Red**: Low confidence (<40%)

## Installation

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Required Packages

Install the following packages using pip:

```bash
pip install flask
pip install tensorflow
pip install Pillow
```

### Alternative Installation

You can also install all dependencies at once:

```bash
pip install flask tensorflow Pillow
```

## Project Structure

```
flask-image-classifier/
│
├── app.py                 # Main Flask application
├── images/                # Directory for uploaded images
├── templates/
│   └── index.html        # HTML template for the web interface
└── README.md             # This file
```

## Usage

### Running the Application

1. Navigate to the project directory:
   ```bash
   cd crowd-counting-experiments/experiments/flask-image-classifier
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your web browser and go to:
   ```
   http://localhost:3000
   ```

### Using the Classifier

1. **Upload Image**: Click "Choose File" and select an image from your computer
2. **Classify**: Click "Predict Image" to get the classification
3. **View Results**: The prediction will appear with color-coded confidence:
   - Green background: High confidence prediction
   - Orange background: Medium confidence prediction
   - Red background: Low confidence prediction

## Technical Details

### Model Information

- **Model**: VGG16 (Visual Geometry Group 16-layer network)
- **Pre-trained on**: ImageNet dataset
- **Input Size**: 224x224 pixels
- **Classes**: 1,000 ImageNet classes

### Image Processing Pipeline

1. **Upload**: Image is uploaded and saved to the `images/` directory
2. **Preprocessing**: 
   - Resize to 224x224 pixels
   - Convert to array format
   - Apply VGG16 preprocessing
3. **Prediction**: Forward pass through VGG16 model
4. **Output**: Decoded predictions with confidence scores

### Confidence Levels

The application categorizes predictions into three confidence levels:

- **Good (≥70%)**: High confidence, reliable predictions
- **Medium (40-70%)**: Moderate confidence, consider with caution
- **Poor (<40%)**: Low confidence, likely unreliable

### Requirements

- Python 3.7+
- Flask
- TensorFlow 2.x
- Pillow (PIL)
- Modern web browser

### **Tutorial Reference**  
- **[Convolutional Neural Networks from Scratch](https://www.youtube.com/watch?v=0nr6TPKlrN0&t=2s)** - YouTube Tutorial
  - Hands on tutorial on how to deploy an ML model with Python using Flask.
