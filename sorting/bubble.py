def bubble_sort(arr):
    loops = 0

    for i, _ in enumerate(arr):
        for j in range(0, len(arr) - i - 1):
            loops += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j +1] = arr[j +1], arr[j]
                swaps = True

        if not swaps:
            break

    print(loops)
    return arr

reversed = [23, 22, 18, 16, 14, 12, 11, 9, 7, 5, 4, 2, -1]
random = [5, 18, 14, 10, 16, 3, -1, 4, 9, 23, 7, 2, 6]
print(bubble_sort(reversed))
print(bubble_sort(random))
