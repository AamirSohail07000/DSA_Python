# Reverse a given list without using the reverse() function


#  Using Slicing (Without reverse())
list1 = [1, 2, 3, 4, 5]
reversed_list = list1[::-1]  # Using slicing to reverse the list
print(reversed_list)

# Using a Loop (Without reverse())

list1 = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(list1) - 1, -1, -1):  # Loop from last index to 0
    reversed_list.append(list1[i])

print(reversed_list)


# Using reverse() Function
list1 = [1, 2, 3, 4, 5]
list1.reverse()  # Modifies the list in place
print(list1)
