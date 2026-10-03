# 🦴 OrthoScan – AI-Assisted X-Ray Fracture Screening

OrthoScan is an AI-powered web application designed to assist in the preliminary screening of bone fractures from X-ray images.

Users can upload an X-ray image and receive an AI-assisted analysis indicating whether a fracture may be present. The project explores the use of artificial intelligence and medical imaging for preliminary fracture screening.

> ⚠️ **Disclaimer:** OrthoScan is an educational and experimental project. It is not a substitute for professional medical diagnosis or medical advice.

## ✨ Features

* 📤 Upload X-ray images for analysis
* 🦴 AI-assisted fracture detection
* 📊 Confidence score for the prediction
* 🔍 Simple and user-friendly interface
* 📋 Analysis history
* 📄 Report generation
* 💻 Responsive web interface

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### AI / Machine Learning

* Python
* Google Colab
* Deep Learning / Image Classification
* FracAtlas Dataset

### Development Tools

* VS Code
* Git
* GitHub
* Google Colab

## 🧠 AI Model Training

The fracture detection model for OrthoScan was trained using **Google Colab**.

The project uses the **FracAtlas dataset**, a publicly available dataset containing annotated musculoskeletal X-ray images for fracture detection research.

### Training Workflow

```text
FracAtlas Dataset
        ↓
Data Preparation
        ↓
Image Preprocessing
        ↓
Train / Validation Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Trained Model
        ↓
OrthoScan Web Application
```

The trained model is integrated into the OrthoScan application to analyze uploaded X-ray images and provide an AI-assisted fracture prediction.

## 🔄 How It Works

```text
        Upload X-Ray
             ↓
      Image Preprocessing
             ↓
       Trained AI Model
             ↓
      Fracture Detection
             ↓
    Prediction + Confidence
             ↓
          Report
```

## 📊 Dataset

**Dataset:** FracAtlas

FracAtlas is used for training and evaluating the fracture detection model.

The dataset contains X-ray images with annotations that can be used for fracture detection and related medical image analysis tasks.

> Dataset source and citation should be included according to the dataset's official usage and licensing requirements.

## 🎯 Project Goal

The goal of OrthoScan is to explore how artificial intelligence can be applied to X-ray image analysis and develop a simple interface for AI-assisted preliminary fracture screening.

The project is intended to demonstrate the potential of AI in medical image analysis while keeping professional medical diagnosis as the responsibility of qualified healthcare professionals.

## 👩‍💻 Team

This project was developed collaboratively by:

* **Vaishnavi Payghan**
* **Divya Ghodke**

## 🚀 Future Improvements

* Improve model performance using larger and more diverse datasets
* Support additional fracture types
* Add explainable AI visualizations such as heatmaps
* Improve report generation
* Add multilingual support
* Deploy the complete application online
* Perform more extensive model validation

## ⚠️ Medical Disclaimer

OrthoScan is developed for educational and research purposes. AI-generated results should not be considered a medical diagnosis. Always consult a qualified healthcare professional for medical evaluation and treatment.

## ⭐ Acknowledgements

This project was developed as a learning and innovation project to explore the application of artificial intelligence and medical image analysis.

