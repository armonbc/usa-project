import csv
import random

# Generate a list of 100 random matches between Player 1 and Player 2
matches = [{"Player 1": random.randint(1, 6), "Player 2": random.randint(1, 6), "Result": ""} for _ in range(100)]

# Save the list of matches to a CSV file
with open("test.csv", "w", newline="") as csvfile:
    fieldnames = ["Player 1", "Player 2", "Result"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for match in matches:
        writer.writerow(match)