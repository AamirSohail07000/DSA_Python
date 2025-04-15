# Square only the odd numbers from 1 to 10. skip even

odd_squares = {num: num**2 for num in range(1, 11) if num % 2 != 0}
print(odd_squares)