# 🎨 Digit Recognition with Custom Neural Network 🤖

This project demonstrates a **digit recognition system** using a neural network implemented from scratch in **NumPy**. The system allows users to draw digits on a canvas and predicts the digit with impressive accuracy. ✏️📊

## 🌟 Project Overview

The project features a **graphical user interface (GUI)** built with **Tkinter**, where users can:

- **Draw Digits**: Use a canvas to draw digits.
- **Predict Digits**: See predictions made by the neural network.
- **Accuracy**: Achieve approximately **90% accuracy** on the MNIST dataset.

## 🧠 Neural Network Implementation

The neural network is implemented using only **NumPy**, with no external deep learning libraries. The architecture includes:

- **Input Layer**: 784 neurons (corresponding to the 28x28 pixel input)
- **Hidden Layer**: 10 neurons
- **Output Layer**: 10 neurons (for the 10 digit classes)

The network uses:

- **ReLU Activation** for the hidden layer
- **Softmax Activation** for the output layer

Training is performed using **gradient descent**.

## 🚀 How It Works

1. **Draw Digit**: Users draw a digit on the canvas.
2. **Predict**: The digit is converted to the MNIST format and predicted by the neural network.
3. **View Results**: The GUI displays the predicted digit and confidence level.

## 📦 Requirements

- Python 3.x
- NumPy
- Pillow
- TensorFlow (for MNIST dataset)

## 🖼️ Results / 📝 Training

![image](https://github.com/user-attachments/assets/d48159b7-564b-4b3b-9c26-0a8e44cbd29b)


### ✏️ Drawn Digit / 🧩 Prediction
![image](https://github.com/user-attachments/assets/81f78d40-e7f9-4194-b317-61ab67101f26)
![image](https://github.com/user-attachments/assets/6b4aa473-937e-4486-b923-6be2b3d6296a)
![image](https://github.com/user-attachments/assets/3a5747b9-53b7-4033-88c1-3633780e973b)
![image](https://github.com/user-attachments/assets/68342112-861d-48f1-a914-16f538a730d8)
![image](https://github.com/user-attachments/assets/0ff4960c-3e15-4a56-9871-452ace75abcb)
![image](https://github.com/user-attachments/assets/495e8ce4-9bdf-426d-bef1-e3355fa3a356)




## 🙏 Acknowledgements

- The MNIST dataset used for training the neural network.
- The NumPy library for implementing the neural network.
- SAMSON ZHANG on Youtube
