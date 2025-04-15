# Square only the even numbers from 1 to 10. Skip odd numbers in the dictionary.

even_squares = {num: num**2 for num in range(1, 11) if num % 2 == 0}
print(even_squares)
