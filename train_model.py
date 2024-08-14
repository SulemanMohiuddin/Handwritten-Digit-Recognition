import numpy as np
import tensorflow as tf
import nn  # Import your neural network code

# Load and preprocess the MNIST dataset using TensorFlow
(X_train, Y_train), (_, _) = tf.keras.datasets.mnist.load_data()
X_train = X_train.reshape(-1, 784).astype(np.float32) / 255.0
Y_train = Y_train.astype(int)  # Replace np.int with int

# Train the model
W1, b1, W2, b2 = nn.gradient_descent(X_train.T, Y_train, alpha=0.1, iterations=500)

# Save the trained parameters
np.savez('model_parameters.npz', W1=W1, b1=b1, W2=W2, b2=b2)

print("Model training complete and parameters saved.")
