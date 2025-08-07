
dict1 = {'apple': 3, 'banana': 2, 'orange': 5}
dict2 = {'banana': 4, 'orange': 1, 'grape': 7}

merged = dict1.copy()  # Start with a copy of the first dict

for key, value in dict2.items():
    # Use the walrus operator to check and update
    if (existing := merged.get(key)) is not None:
        merged[key] = existing + value  # On conflict: sum the values
    else:
        merged[key] = value  # New key: just add

print("✅ Merged dictionary with conflict resolution:")
print(merged)
