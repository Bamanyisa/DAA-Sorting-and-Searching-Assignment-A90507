def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_values = max_val - min_val + 1
    count = [0] * range_of_values

    for num in arr:
        count[num - min_val] += 1

    sorted_arr = []
    for i in range(range_of_values):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr

#Example
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)
