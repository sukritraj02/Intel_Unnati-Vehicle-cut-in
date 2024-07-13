import os
import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image

def calculate_ttc(speed, distance):
    if speed > 0:
        return distance / speed
    return float('inf')

def check_collision_alert(ttc, threshold=3):
    if ttc < threshold:
        return "Danger"
    return "Safe"

app = Flask(__name__)
CORS(app)

# Load the trained model
model = tf.keras.models.load_model('cut_in_detection_model.h5')

def preprocess_image(image):
    image = image.resize((128, 128))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    image = Image.open(file.stream)
    processed_image = preprocess_image(image)
    
    prediction = model.predict(processed_image)
    label = 'Cut-In' if prediction[0][0] > 0.5 else 'No Cut-In'
    
    speed = float(request.form['speed'])
    distance = float(request.form['distance'])
    ttc = calculate_ttc(speed, distance)
    alert = check_collision_alert(ttc)
    
    return jsonify({
        'prediction': label,
        'ttc': ttc,
        'alert': alert
    })

if __name__ == '__main__':
    app.run(debug=True)
