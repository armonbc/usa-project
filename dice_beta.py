import numpy as np
import csv

# Define the mapping of labels to numerical values
label_map = {'P1': 0, 'P2': 1, 'Draw': 2}

# Load the training data
train_data = []
with open('trained.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        p1_score, p2_score, label = row
        train_data.append([int(p1_score), int(p2_score), label_map[label]])

# Load the test data
test_data = []
with open("test.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        p1_score, p2_score, _ = row
        test_data.append([int(p1_score), int(p2_score)])

# Convert the data to numpy arrays
train_data = np.array(train_data)
test_data = np.array(test_data)

# Split the data into input (X) and output (y) variables
train_x = train_data[:, :2]
train_y = train_data[:, 2]
test_x = test_data[:, :2]

# Normalize the input data
train_x = train_x / 6.0
test_x = test_x / 6.0

# Define the softmax activation function
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

# Define the neural network weights
w = np.random.randn(2, 3)
b = np.zeros((1, 3))

# Train the neural network
epochs = 5000
lr = 0.1
for i in range(epochs):
    z = np.dot(train_x, w) + b
    a = softmax(z)
    dz = a - np.eye(3)[train_y]
    dw = np.dot(train_x.T, dz)
    db = np.sum(dz, axis=0, keepdims=True)
    w = w - lr * dw
    b = b - lr * db

# Evaluate the neural network on the test data
z = np.dot(test_x, w) + b
a = softmax(z)
result = np.argmax(a, axis=1)

# Map the numerical labels back to string labels
result = [key for key, value in label_map.items() for r in result if value == r]

# Save the results to a CSV file
with open('beta_output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Player 1', 'Player 2', 'Result'])
    for i in range(len(test_data)):
        writer.writerow([test_data[i][0], test_data[i][1], result[i]])