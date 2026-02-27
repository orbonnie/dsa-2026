def pivot(arr, start = 0, end = None):
    """Finds the correct sorted index for the start value,
       shifts all lower values to the left of sorted index
       and returns the sorted index
    """
    if not end:
        end = len(arr) - 1

    pivot = arr[start]
    swap_idx = start

    for i in range(start + 1, end + 1):
        if pivot > arr[i]:
            swap_idx += 1
            arr[i], arr[swap_idx] = arr[swap_idx], arr[i]

    arr[start], arr[swap_idx] = arr[swap_idx], arr[start]

    return swap_idx



def quick_sort(arr, left = 0, right = None):
    """Inserts each array value into its correct sorted index
       and shifts lower values to the left of the sorted index.
       Returns the sorted array when sub array is empty.
    """
    if not right:
        right = len(arr) - 1

    if left < right:
        pivot_idx = pivot(arr, left, right)
        quick_sort(arr, left, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, right)

    return arr


print(pivot([4, 8, 2, 1, 5, 7, 6, 3]))

arr = [4, 8, 2, 1, 5, 7, 6, 3]

print(quick_sort(arr, 0, len(arr) - 1))
