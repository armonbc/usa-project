# Load necessary libraries
library(nnet)
# load the ggplot2 library
library(ggplot2)

# Read in the data
train_data <- read.csv("trained.csv", header = TRUE)
test_data <- read.csv("test.csv", header = TRUE)

# Prepare the training data
train_x <- as.matrix(train_data[,1:2])
train_y <- ifelse(train_data[,3] == "P1", 1, ifelse(train_data[,3] == "P2", 2, 3))

# Train the neural network
model <- nnet(train_x, train_y, size=3, linout = TRUE)

# Prepare the test data
test_x <- as.matrix(test_data[,1:2])

# Make predictions on the test data
pred_y <- predict(model, test_x)
pred_y <- ifelse(pred_y < 1.5, "P1", ifelse(pred_y < 2.5, "P2", "Draw"))

# Combine the predictions with the test data and save to file
output_data <- cbind(test_x, pred_y)
write.csv(output_data, "r_output.csv", row.names = FALSE)

# read the output csv file
output_data <- read.csv("r_output.csv")