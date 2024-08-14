import tensorflow as tf
import matplotlib.pyplot as plt

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# Define the number of images to display
num_images = 5

# Create a figure with subplots
plt.figure(figsize=(10, 5))

# Loop to display multiple images
for i in range(num_images):
    plt.subplot(1, num_images, i + 1)
    plt.imshow(train_images[i], cmap='gray')
    plt.title(f'Label: {train_labels[i]}')
    plt.axis('off')

# Show the plot
plt.show()
