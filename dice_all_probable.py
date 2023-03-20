import random
import csv

# Generate all possible combinations of two dice rolls
combos = [(i, j) for i in range(1, 7) for j in range(1, 7)]

# Initialize an empty list to store the results as dictionaries
results = []

# Loop through each combination of rolls and determine the winner
for combo in combos:
    if combo[0] > combo[1]:
        result = "P1"
    elif combo[0] < combo[1]:
        result = "P2"
    else:
        result = "Draw"
    
    # Add the result as a dictionary item to the list
    result_dict = {"Player 1": combo[0], "Player 2": combo[1], "Result": result}
    results.append(result_dict)
    
    with open("trained.csv", "w", newline="") as csvfile:
       fieldnames = ["Player 1", "Player 2", "Result"]
       writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
       writer.writeheader()
       for result in results:
          writer.writerow(result)

# Print the list of dictionary items
print(results)