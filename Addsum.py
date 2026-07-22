def find_even_numbers(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count

# Call the function
numbers = [4,5,7,8,5,10,12]
result = find_even_numbers(numbers)
print(result)