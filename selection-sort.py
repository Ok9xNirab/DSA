def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i}: {min_index}")

selection_sort([64, 25, 12, 22, 11])