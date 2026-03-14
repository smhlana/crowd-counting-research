from flask import Flask, render_template, request
import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
import torchvision.transforms as transforms
import os

# CNN Model Architecture (copy from Colab notebook)
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)  # 3 input channels, 6 output channels, 5x5 kernel
        self.pool1 = nn.MaxPool2d(2, 2)  # 2x2 kernel, stride of 2
        self.conv2 = nn.Conv2d(6, 16, 5)  # 6 input channels, 16 output channels, 5x5 kernel
        self.pool2 = nn.MaxPool2d(2, 2)  # 2x2 kernel, stride of 2
        self.fc1 = nn.Linear(16 * 5 * 5, 120)  # Flattening the input
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)  # 10 output classes for CIFAR-10

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = self.pool2(x)
        x = x.view(-1, 16 * 5 * 5)  # Flatten for fully connected layer
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        return x

# CIFAR-10 class labels
CIFAR10_CLASSES = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Load your trained model
model = CNN()
model.load_state_dict(torch.load('cifar10_cnn_state_dict.pth', map_location='cpu'))
model.eval()

# Image preprocessing for CIFAR-10 (32x32 input size)
transform = transforms.Compose([
    transforms.Resize((32, 32)),  # CIFAR-10 uses 32x32 images
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

INDEX_TEMPLATE = 'index.html'
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']

    if not imagefile or imagefile.filename == '':
        app.logger.info("No image uploaded")
        return render_template(INDEX_TEMPLATE, prediction=None, confidence_level=None, 
                             error="No image uploaded. Please select an image to upload.")
    
    try:
        # Save uploaded image
        image_path = "./images/" + imagefile.filename
        imagefile.save(image_path)

        # Load and preprocess image
        image = Image.open(image_path).convert('RGB')
        image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

        # Make prediction
        with torch.no_grad():
            outputs = model(image_tensor)
            probabilities = F.softmax(outputs, dim=1)
            confidence, predicted_class = torch.max(probabilities, 1)
            
            predicted_label = CIFAR10_CLASSES[predicted_class.item()]
            confidence_percentage = confidence.item() * 100

        # Determine confidence level for color coding
        if confidence_percentage >= 70:
            confidence_level = "good"
        elif confidence_percentage >= 40:
            confidence_level = "medium"
        else:
            confidence_level = "poor"

        classification = f"{predicted_label} ({confidence_percentage:.2f}%)"
        
        # Clean up - delete uploaded image
        os.remove(image_path)
        
        return render_template(INDEX_TEMPLATE, prediction=classification, 
                             confidence_level=confidence_level, error=None)
    
    except Exception as e:
        # Clean up on error
        if 'image_path' in locals() and os.path.exists(image_path):
            os.remove(image_path)
        return render_template(INDEX_TEMPLATE, prediction=None, confidence_level=None,
                             error=f"Error processing image: {str(e)}")

if __name__ == '__main__':
    app.run(port=3000, debug=True)