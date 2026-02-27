def insertion_sort(arr):
    """compares each index to the values on its left and
       inserts it where it belongs among those values
    """
    for i in range(1, len(arr)):
        for j in reversed(range(1, i + 1)):
            last_larger = j
            delta = 1
            while (arr[j] < arr[j - delta]) and j - delta >= 0:
                last_larger = j - delta
                delta -= 1

            if last_larger != j:
                arr[j], arr[last_larger] = arr[last_larger], arr[j]

    return arr


random = [15, 2, 7, 4, 3, 10, 22, 6]

print(insertion_sort([0, 4, 3, 1, 2]))
print(insertion_sort([10, 1, 9, 2, 8, 3]))
print(insertion_sort([10, 9, 1, 8, 2, 3]))
print(insertion_sort(random))