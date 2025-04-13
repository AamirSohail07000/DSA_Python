# Create a dictionary where keys are numbers from 1 to 5 and values are their cubes. 📌 Expected Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125} 

# Creating dictionary using comprehension
cube_dict = {x: x**3 for x in range(1, 6)}

# Printing the result
print(cube_dict)
