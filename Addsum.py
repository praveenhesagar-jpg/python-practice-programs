def find_even_numbers(arr):
    total =0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total

# Call the function
numbers = [4,5,7,8,5,10,12]
result = find_even_numbers(numbers)
print(result)