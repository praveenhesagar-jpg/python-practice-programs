def find_second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements for a second largest

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None

# Call the function
numbers = [10, 5, 8, 12, 3]                
second_largest = find_second_largest(numbers)
print("Second largest number is:", second_largest)