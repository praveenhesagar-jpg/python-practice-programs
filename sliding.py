def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None
    first_window_sum = sum(arr[:k])
    max_sum = first_window_sum
    for i in range(k, n):
        first_window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, first_window_sum)
    return max_sum      

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3   
result = max_sum_subarray(arr, k)
print(result)