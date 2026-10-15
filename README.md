# 🖐️ Gender Detection Using Fingerprint

A machine learning-based web application that uses a Convolutional Neural Network (CNN) to predict gender from fingerprint images. Developed using Python and Flask, the application provides an easy-to-use interface for uploading fingerprint images, viewing prediction results, and checking prediction history.

## 📌 Project Overview

This project explores fingerprint image classification using deep learning techniques. The system preprocesses uploaded fingerprint images and passes them to a trained CNN model to generate a gender prediction.

The application uses SQLite to store prediction records, allowing users to view previous results.

## ✨ Features

- 📤 Upload fingerprint images for prediction
- 🤖 CNN-based fingerprint image classification
- 🖼️ Image preprocessing using OpenCV
- 📊 Display predicted gender results
- 📜 View prediction history
- 🔄 Upload another image easily
- 🗄️ Store prediction records using SQLite
- 🌐 Simple web interface built with HTML and CSS
- ✅ Validate uploaded image formats

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| TensorFlow / Keras | CNN model development and prediction |
| OpenCV | Image processing |
| NumPy | Numerical operations |
| SQLite | Store prediction history |
| HTML | Web page structure |
| CSS | User interface styling |

## ⚙️ How It Works

1. **Upload Image:** The user selects a fingerprint image.
2. **Image Preprocessing:** The image is converted to grayscale and resized to the model's expected input dimensions.
3. **Model Prediction:** The processed image is passed to the trained CNN model.
4. **Display Result:** The application displays the predicted class.
5. **Save History:** The prediction details are stored in the SQLite database.
6. **View History:** The user can review previous prediction records.

## 📂 Project Structure

```text
Gender_detection/
│
├── app.py
├── model/
│   └── fingerprint_gender_model.h5
├── templates/
│   ├── index.html
│   ├── result.html
│   └── history.html
├── static/
│   ├── style.css
│   └── 3409297.jpg
├── uploads/
├── fingerprint_results.db
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: Adjust the structure above to match the actual files and folders in your project. Do not upload private files or unnecessary generated data.*

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shubham-2691/Gender_detection.git
```

### 2. Open the Project Directory

```bash
cd Gender_detection
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Ensure that the required libraries and compatible versions are listed in `requirements.txt`.

### 5. Prepare the Model

Place the trained model file at the path expected by the application:

```text
model/fingerprint_gender_model.h5
```

If the model is not included in the repository, obtain it separately and place it in the required location.

### 6. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## 🧪 Supported Image Formats

The application can accept the following formats, subject to its upload validation:

- JPG
- JPEG
- PNG
- BMP

## 🗄️ Database

The application uses SQLite to store prediction records. The database keeps information such as the uploaded filename and predicted class, according to the application's implementation.

## 🎯 Project Objectives

- Explore deep learning for fingerprint image classification.
- Develop a web interface for image-based prediction.
- Integrate a trained CNN model with Flask.
- Apply image preprocessing techniques using OpenCV.
- Store and retrieve prediction history using SQLite.

## ⚠️ Limitations

- Prediction quality depends on the training dataset, model performance, and input image quality.
- Results are model predictions and may be incorrect.
- Fingerprint-based gender prediction is not a definitive or validated method of determining a person's gender.
- This project is intended for educational and experimental purposes, not for identity verification or consequential decisions.

## 🔮 Future Enhancements

- Improve model performance through further training and evaluation.
- Add prediction confidence scores and evaluation metrics.
- Improve error handling and image validation.
- Enhance the user interface and accessibility.
- Support additional image analysis and visualization features.

## 👨‍💻 Author

**Shubham Patil**

AI & Data Science Student

## 📄 License

This project is intended for educational purposes. Add a suitable open-source license if you want others to reuse or distribute the code.

---

⭐ If you find this project interesting, feel free to explore the source code and learn more about Flask, CNNs, and image processing.
