def maximum_even_number(numbers):
    maximum = None
    for num in numbers:
        if num % 2 == 0:
            if maximum is None or num > maximum:
                maximum = num
    return maximum


numbers = [3, 7, 2, 8, 5, 10, 20, 1]
result = maximum_even_number(numbers)
print(result)