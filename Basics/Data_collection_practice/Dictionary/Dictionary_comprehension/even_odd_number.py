# Create a dictionary with numbers 1 to 10 as keys and whether each is "even" or "odd" as the value. 
# 📌 Expected Output: {1: 'odd', 2: 'even', 3: 'odd', ...}

number_type = {num: 'even' if num % 2 == 0 else 'odd' for num in range(1, 11)}
print(number_type)
