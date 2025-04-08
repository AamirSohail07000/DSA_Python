# Checking Membership
# Check if the number 7 is present in a given set {1, 2, 3, 4, 5}.

# Method 1
# Using in keyword (Recommended & Efficient)
my_set = {1, 2, 3, 4, 5, 7}
if 7 in my_set:
    print("7 is present.")
else:
    print("7 is not present.")

# Fastest and cleanest way (O(1) time in sets).

# Method 2
# Using a loop (Without in keyword)
my_set = {1, 2, 3, 4, 5}
found = False

for num in my_set:
    if num == 7:
        found = True
        break

if found:
    print("7 is present.")
else:
    print("7 is not present.")

# Not efficient for large sets — but useful if in is not allowed.

