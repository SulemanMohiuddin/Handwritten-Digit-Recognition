import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import nn  # Ensure this is the correct path to your neural network code

class DrawDigitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Draw a Digit")
        self.canvas = tk.Canvas(root, width=280, height=280, bg="white")
        self.canvas.pack()

        # Buttons for Save and Clear
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.save_button = tk.Button(self.button_frame, text="Save and Predict", command=self.save_and_predict)
        self.save_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)

        # Labels for prediction and confidence
        self.prediction_label = tk.Label(root, text="Draw a digit and click 'Save and Predict'")
        self.prediction_label.pack()

        self.confidence_label = tk.Label(root, text="")
        self.confidence_label.pack()

        self.drawing = Image.new("L", (280, 280), 255)
        self.draw = ImageDraw.Draw(self.drawing)
        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")
        self.draw.ellipse([x-5, y-5, x+5, y+5], fill=0)

    def save_and_predict(self):
        # Save the image
        image = ImageOps.fit(self.drawing, (28, 28), method=0, bleed=0.0, centering=(0.5, 0.5))
        image = ImageOps.invert(image)  # MNIST images are white digits on black background
        image = np.array(image) / 255.0
        image = image.reshape(784, 1)  # Ensure the shape is (784, 1)

        # Load model parameters
        params = np.load('model_parameters.npz')
        W1 = params['W1']
        b1 = params['b1']
        W2 = params['W2']
        b2 = params['b2']

        # Predict the digit
        Z1, A1, Z2, A2 = nn.forward_prop(W1, b1, W2, b2, image)  # Forward prop to get A2
        prediction = nn.get_predictions(A2)
        confidence = np.max(A2)  

        self.prediction_label.config(text=f"Predicted digit: {prediction[0]}")
        self.confidence_label.config(text=f"Confidence: {confidence:.2f}")

    def clear_canvas(self):
        # Clear the canvas and reset the drawing image
        self.canvas.delete("all")
        self.drawing = Image.new("L", (280, 280), 255)
        self.draw = ImageDraw.Draw(self.drawing)
        self.prediction_label.config(text="Draw a digit and click 'Save and Predict'")
        self.confidence_label.config(text="")

root = tk.Tk()
app = DrawDigitApp(root)
root.mainloop()
