from flask import Flask, render_template, request

from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions, VGG16

INDEX_TEMPLATE = 'index.html'
model = VGG16()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template(INDEX_TEMPLATE, prediction=None, confidence_level=None, error=None)

@app.route('/predict', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']

    if not imagefile or imagefile.filename == '':
        app.logger.info("No image uploaded")
        return render_template(INDEX_TEMPLATE, prediction=None, confidence_level=None, error="No image uploaded. Please select an image to upload.")
    
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    yhat = model.predict(image)
    label = decode_predictions(yhat)
    label = label[0][0]

    classification = "%s (%.2f%%)" % (label[1], label[2]*100)
    
    # Determine confidence level for color coding
    confidence_percentage = label[2]*100
    if confidence_percentage >= 70:
        confidence_level = "good"
    elif confidence_percentage >= 40:
        confidence_level = "medium"
    else:
        confidence_level = "poor"
    
    return render_template(INDEX_TEMPLATE, prediction=classification, confidence_level=confidence_level, error=None)

if __name__ == '__main__':
    app.run(port=3000, debug=True)