def find_odd_numbers(arr):
    count =0
    for num in arr:
        if num % 2 !=0:
            count += 1
    return count
        

# Call the function
numbers = [5,4,8,3,11,17,21]
odd_count = find_odd_numbers(numbers)
print(  "odd numbers are", odd_count)
