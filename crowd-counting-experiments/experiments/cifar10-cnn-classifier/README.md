# CIFAR-10 CNN Classifier

A web-based image classification application built with Flask and PyTorch that uses a custom-trained Convolutional Neural Network (CNN) to classify images into one of 10 CIFAR-10 categories.

## 🎯 Project Overview

This project implements a **custom CNN architecture trained from scratch** on the CIFAR-10 dataset. Unlike pre-trained models, this CNN was built and trained specifically for the 10 CIFAR-10 classes, providing hands-on experience with deep learning fundamentals.

## 🔧 Model Architecture

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

## 🏷️ Classification Categories

The model can classify images into these 10 CIFAR-10 categories:

| Category | Icon | Category | Icon |
|----------|------|----------|------|
| ✈️ Plane | 🚗 Car | 🐦 Bird | 🐱 Cat | 
| 🦌 Deer | 🐕 Dog | 🐸 Frog | 🐴 Horse |
| 🚢 Ship | 🚛 Truck | | |

## 🌈 Features

- **Custom CNN Model**: Built and trained from scratch (not pre-trained)
- **Real-time Classification**: Upload and classify images instantly
- **Confidence Visualization**: Color-coded confidence levels
  - 🟢 **Green**: High confidence (≥70%)
  - 🟠 **Orange**: Medium confidence (40-70%)
  - 🔴 **Red**: Low confidence (<40%)
- **Responsive Design**: Modern Bootstrap UI with gradient styling
- **Error Handling**: Comprehensive error messages and validation
- **Automatic Cleanup**: Uploaded images are automatically deleted after processing

## 📋 Prerequisites

- **Python 3.7+**
- **PyTorch** (CPU version is sufficient for inference)
- **Flask** for the web application
- **Pillow** for image processing

## 🚀 Installation

### 1. Install Dependencies

```bash
# Navigate to project directory
cd crowd-counting-experiments/experiments/cifar10-cnn-classifier

# Install required packages
pip install -r requirements.txt
```

### 2. Add Your Trained Model

You need to place your trained model file in the project directory:

```bash
# Copy your trained model from Google Colab downloads
# Place: cifar10_cnn_state_dict.pth in the project root
```

### 3. Update Model Loading

Uncomment these lines in `app.py`:
```python
# Uncomment these lines:
model.load_state_dict(torch.load('cifar10_cnn_state_dict.pth', map_location='cpu'))
model.eval()
```

## 🏃‍♂️ Running the Application

```bash
# Run the Flask application
python app.py
```

**Access the application:**
- Open browser: `http://localhost:3001`
- Upload an image
- Get instant classification results!

## 📁 Project Structure

```
cifar10-cnn-classifier/
│
├── app.py                          # Flask application with PyTorch model
├── requirements.txt                # Project dependencies
├── README.md                       # This documentation
├── cifar10_cnn_state_dict.pth     # Your trained model (add this)
│
├── templates/
│   └── index.html                  # Web interface template
│
└── images/                         # Temporary storage for uploads
```

## 🎨 Model Training (Google Colab)

This model was trained using the CNN architecture defined in the Colab notebook:

### Training Process:
1. **Data Loading**: CIFAR-10 dataset with data augmentation
2. **Architecture**: Custom CNN with 2 conv layers + 3 FC layers  
3. **Training**: Multiple epochs with loss/accuracy monitoring
4. **Validation**: Test set evaluation for performance metrics

### To Save Your Model:
```python
# In Google Colab after training:
torch.save(model.state_dict(), 'cifar10_cnn_state_dict.pth')
from google.colab import files
files.download('cifar10_cnn_state_dict.pth')
```

## 🔍 Usage Tips

### Best Results:
- **Small objects**: Works best with simple, centered objects
- **Clear images**: Avoid blurry or heavily edited images
- **CIFAR-10 style**: Similar to 32×32 simple object images
- **Single subjects**: One main object per image

### Image Guidelines:
- **Format**: JPG, PNG, GIF supported
- **Size**: Any size (automatically resized to 32×32)
- **Content**: Objects from the 10 CIFAR-10 categories

## 🔧 Customization

### Modify Confidence Thresholds:
```python
# In app.py, adjust these values:
if confidence_percentage >= 70:    # High confidence
    confidence_level = "good"
elif confidence_percentage >= 40:  # Medium confidence  
    confidence_level = "medium"
else:                             # Low confidence
    confidence_level = "poor"
```

### Change Port:
```python
# In app.py:
app.run(port=3001, debug=True)  # Change port number
```

## 🐛 Troubleshooting

### Common Issues:

1. **Model Not Found Error**
   ```
   FileNotFoundError: cifar10_cnn_state_dict.pth
   ```
   **Solution**: Download your trained model from Colab and place in project root

2. **PyTorch Not Installed**
   ```
   ModuleNotFoundError: No module named 'torch'
   ```
   **Solution**: `pip install torch torchvision`

3. **Port Already in Use**
   ```
   Address already in use
   ```
   **Solution**: Change port in `app.py` or stop other Flask apps

4. **Low Accuracy**
   - Model may need more training epochs
   - Try images more similar to CIFAR-10 style
   - Check if model weights loaded correctly

## 📊 Performance Notes

- **Accuracy**: Depends on your training results
- **Speed**: Fast inference on CPU (~100ms per image)
- **Memory**: Lightweight model (~1MB state dict)
- **Input**: Optimized for 32×32 images (CIFAR-10 format)

## 🎓 Learning Outcomes

This project demonstrates:
- **Custom CNN Architecture**: Building neural networks from scratch
- **PyTorch Training**: Complete training pipeline implementation  
- **Model Deployment**: Converting trained models to web applications
- **Full-Stack Integration**: Connecting ML models with web frameworks
- **Image Processing**: Preprocessing pipelines for deep learning

## 📄 License

This project is for educational purposes as part of crowd counting and computer vision research experiments.

## 🤝 Contributing

This is a research/educational project. For questions or improvements:
1. Test thoroughly with different image types
2. Document any modifications to the CNN architecture
3. Update requirements.txt for new dependencies

---

**Built with ❤️ for learning PyTorch and computer vision fundamentals.**