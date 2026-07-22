def two_sum(arr, target):

    for i in range(len(arr)):

        needed = target - arr[i]

        for j in range(i + 1, len(arr)):

            if arr[j] == needed:

                return [i, j]
            
arr = [2, 7, 11, 15]
target = 13

print(two_sum(arr, target))