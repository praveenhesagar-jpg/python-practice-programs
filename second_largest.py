def find_second_largest(arr):
    largest = None
    second_largest = None

    for num in arr:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or (num > second_largest and num != largest):
            second_largest = num

    return second_largest


# Call the function
numbers = [9, 9]

second_largest = find_second_largest(numbers)
print("Second largest number is:", second_largest)