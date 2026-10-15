import os
import sqlite3
import numpy as np
from flask import Flask, request, render_template, redirect, url_for, flash
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image  # PIL supports multiple image formats

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "shubham"  # Required for flash messages

# Load the trained gender detection model
MODEL_PATH = r""
model = load_model(MODEL_PATH)

# Database setup
DB_PATH = "fingerprint_results.db"

def init_db():
    """Initialize the database and create the table if it doesn't exist."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS predictions 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           filename TEXT, 
                           gender TEXT)''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# Initialize the database
init_db()

# Ensure the uploads folder exists for storing uploaded images
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to preprocess images before making predictions
def preprocess_image(image_path):
    img_size = 96  # Resize images to 96x96
    try:
        img = Image.open(image_path).convert('L')  # Convert to grayscale
        img = img.resize((img_size, img_size))  # Resize image
        img = img_to_array(img)  # Convert image to array
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        img = img / 255.0  # Normalize pixel values
        return img
    except Exception as e:
        print(f"Error processing image: {e}")
        return None  # Return None if the image is not valid

# Home route to display the main page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle file upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        flash("No file uploaded", "error")
        return redirect(url_for('home'))

    file = request.files['file']
    if file.filename == '':
        flash("No file selected", "error")
        return redirect(url_for('home'))

    # Save the uploaded file in the uploads folder
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Preprocess the image
    img = preprocess_image(file_path)
    if img is None:
        os.remove(file_path)  # Remove invalid image file
        flash("Invalid image file", "error")
        return redirect(url_for('home'))

    # Predict gender using the trained model
    prediction = model.predict(img)[0][0]
    gender = 'Male' if prediction < 0.5 else 'Female'

    # Store the result in the database
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO predictions (filename, gender) VALUES (?, ?)", (file.filename, gender))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

    # Redirect to the result page with prediction data
    return redirect(url_for('result', gender=gender, filename=file.filename))

# Route to display the prediction result
@app.route('/result')
def result():
    """Display the result after prediction."""
    gender = request.args.get('gender', 'Unknown')
    filename = request.args.get('filename', 'Unknown')

    # Debugging: Print filename and gender to check values
    print(f"DEBUG: Filename - {filename}, Gender - {gender}")

    return render_template('result.html', gender=gender, filename=filename)

# Route to display the last 10 stored predictions
@app.route('/results')
def results():
    """Retrieve and display the last 10 stored results."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT filename, gender FROM predictions ORDER BY id DESC LIMIT 10")  
        history = cursor.fetchall()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        history = []

    return render_template('results.html', history=history)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
