def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements

    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    result = second_largest if second_largest != float('-inf') else None

    if result is not None:
        print("Second largest number is:", result)
    else:
        print("No second largest number found.")
    print("----------------------")

    return result

nums = [10, 4, 23, 7, 23, 15.5]
result = find_second_largest(nums)


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict1 | dict2

print("Merged dictionary:", merged_dict)
'''
numbers = [12, 45, 2, 41, 31, 90, 90]

unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("No second largest number found.")
else:
    
    unique_numbers.sort(reverse=True)
    
    print("Second largest number:", unique_numbers[1])


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict1 | dict2

print("Merged dictionary:", merged_dict)
'''