# From a dictionary of names and ages, filter out only people who are 18 or older.

ages = {
    "Alice": 17,
    "Bob": 21,
    "Charlie": 15,
    "David": 19,
    "Eve": 22
}

adults = {name: age for name, age in ages.items() if age >= 18}

print(adults)
