# Python program to perform Union, Intersection, and Difference on two sets: {1, 2, 3, 4} and {3, 4, 5, 6}

# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)

# Intersection
intersection_set = set1.intersection(set2)

# Difference (elements in set1 but not in set2)
difference_set = set1.difference(set2)

# Display the results
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (set1 - set2):", difference_set)
