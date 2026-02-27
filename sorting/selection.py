def selection_sort(arr, comp = True):
    def cmp(a, b):
        return a < b if comp  else  a > b

    for i, _ in enumerate(arr):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if cmp(arr[j], arr[min_idx]):
                min_idx = j

        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

random = [15, 2, 7, 4, 3, 10, 22, 6]

print(selection_sort(random, False))