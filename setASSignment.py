# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Get the union of the two sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Get the intersection of the two sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Update set1 with elements in set2
set1.update(set2)
print("Updated set1:", set1)

# Get the symmetric difference between set1 and set2
symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric difference between set1 and set2:", symmetric_difference)

# Create another set3
set3 = {9, 10, 11}

# Clear set3
set3.clear()
print("Cleared set3:", set3)
