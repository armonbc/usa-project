import csv
import numpy as np

# Load the training data from train.csv
train_data = []
with open("trained.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert the row values from strings to integers
        row["Player 1"] = int(row["Player 1"])
        row["Player 2"] = int(row["Player 2"])
        if row["Result"] == "P1":
            row["Result"] = 1
        elif row["Result"] == "P2":
            row["Result"] = 0
        else:
            row["Result"] = 0.5
        train_data.append(row)

# Load the test data from test.csv
test_data = []
with open("test.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert the row values from strings to integers
        row["Player 1"] = int(row["Player 1"])
        row["Player 2"] = int(row["Player 2"])
        row["Result"] = -1
        test_data.append(row)

# Convert the data to numpy arrays
train_x = np.array([(d["Player 1"], d["Player 2"]) for d in train_data])
train_y = np.array([d["Result"] for d in train_data])
test_x = np.array([(d["Player 1"], d["Player 2"]) for d in test_data])

# Define the neural network model
input_dim = 2
output_dim = 1
hidden_dim = 10
model = np.random.randn(input_dim, hidden_dim)
bias = np.random.randn(output_dim)

# Define the activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Train the neural network on the training data
epochs = 10000
learning_rate = 0.1
for epoch in range(epochs):
    # Forward pass
    z = np.dot(train_x, model) + bias
    a = sigmoid(z)
    # Backward pass
    error = train_y.reshape(-1, 1) - a
    d = error * a * (1 - a)
    delta = np.dot(train_x.T, d)
    model += learning_rate * delta
    bias += learning_rate * np.sum(d)

# 1. Make predictions on the test data
predictions = []
for c in range(1,20):
   for i in range(len(test_data)):
     x = test_x[i]
     z = np.dot(x, model) + bias
     a = sigmoid(z)
    

# 2. Make predictions on the test data
predictions = []
for i in range(len(test_data)):
    x = test_x[i]
    z = np.dot(x, model) + bias
    a = sigmoid(z)
    print(x)
    print(z)
    print(a)
    print(np.isclose(a, 0.5, rtol=1e-01))
    print("\n")
    result = np.select([a > 0.70, a < 0.30, np.isclose(a, 0.5, rtol=1e-01)], ["P1", "P2", "Draw"])
    test_data[i]["Result"] = result[0]
    predictions.append(test_data[i])

# Save the predictions to a CSV file
with open("output.csv", "w", newline="") as csvfile:
    fieldnames = ["Player 1", "Player 2", "Result"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for prediction in predictions:
        writer.writerow(prediction)

# Results
# print(predictions)