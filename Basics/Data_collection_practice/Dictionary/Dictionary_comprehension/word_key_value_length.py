# Given a list of words, create a dictionary with each word as a key and its length as value: 
# words = ['apple', 'banana', 'cherry'] # Output: {'apple': 5, 'banana': 6, 'cherry': 6} 

words = ['apple', 'banana', 'cherry']

word_lengths = {word: len(word) for word in words}

print(word_lengths)
