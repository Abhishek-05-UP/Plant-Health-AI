🌿 AI Plant Health Detector

An AI-powered application for detecting plant diseases using leaf images.

📌 About the Project

The AI Plant Health Detector is a deep learning-based project designed to identify plant diseases by analyzing images of plant leaves. Users can upload a leaf image, and the trained AI model predicts the corresponding plant condition.

The main goal of this project is to help identify potential plant diseases quickly and support healthier plant growth using Artificial Intelligence.

🎯 Objectives

- Detect plant diseases from leaf images.
- Identify healthy and diseased plants.
- Demonstrate the practical use of AI and deep learning in agriculture.
- Provide a simple, user-friendly interface for plant health prediction.

⚙️ How It Works

1. Upload Image: The user uploads an image of a plant leaf.
2. Image Preprocessing: The image is resized to the required dimensions of 224 × 224 pixels.
3. AI Prediction: The trained MobileNetV2 model analyzes the image.
4. Classification: The model predicts the most likely plant disease or healthy condition.
5. Display Result: The application displays the predicted class and confidence score.

🧠 Technologies Used

- Python — Core programming language.
- TensorFlow / Keras — Building and running the deep learning model.
- MobileNetV2 — Pre-trained convolutional neural network used for image classification.
- PlantVillage Dataset — Dataset used for model training.
- Streamlit — Web interface for uploading images and viewing predictions.

📊 Model Information

- Model: MobileNetV2 with transfer learning
- Input Image Size: 224 × 224 pixels
- Number of Classes: 38
- Dataset Size: 54,305 images
- Validation Accuracy: Approximately 95.3% during training

Note: Validation accuracy represents performance on the validation dataset. Real-world accuracy may differ, and predictions can sometimes be incorrect.

🌱 Supported Plants and Conditions

The model covers 38 classes involving plants such as:

- Apple
- Blueberry
- Cherry
- Corn
- Grape
- Orange
- Peach
- Bell Pepper
- Potato
- Raspberry
- Soybean
- Squash
- Strawberry
- Tomato

These classes include various diseases and healthy leaf conditions.

🚀 How to Run the Project

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd Plant_Health_AI

2. Create and activate a virtual environment

py -3.12 -m venv .venv
.venv\Scripts\activate

3. Install the required libraries

pip install streamlit tensorflow pillow numpy

4. Start the application

streamlit run app.py

Open the local URL displayed in the terminal to access the application.

Requirements: Keep "app.py", "class_names.json", and the trained model file in the locations expected by your code. Install any additional dependencies imported by your application.

⚠️ Limitations

- Predictions depend on image quality, lighting, leaf condition, and similarity to training images.
- The model may misclassify unfamiliar plants or diseases.
- The system is intended as a preliminary screening tool, not a replacement for expert agricultural diagnosis.
- The model has been trained on a specific set of 38 classes and cannot reliably identify conditions outside those classes.

🔮 Future Improvements

- Improve prediction accuracy on real-world leaf images.
- Add treatment suggestions for detected diseases.
- Support more plant species and diseases.
- Deploy the application online for easy access.
- Develop a mobile-friendly version.

👨‍💻 Conclusion

The AI Plant Health Detector demonstrates how deep learning and computer vision can be applied to agriculture. By analyzing leaf images, the application provides a convenient way to identify potential plant health problems and encourages the use of AI in smarter farming.

Built with Python, TensorFlow, MobileNetV2, and Streamlit. 🌿
