from math import floor, ceil

def merge_lists(arr1, arr2):
    """Merge two sorted lists"""
    merged_arr = []
    arr1_ind = 0
    arr2_ind = 0

    while arr1_ind < len(arr1) and arr2_ind < len(arr2):
        if arr1[arr1_ind] <= arr2[arr2_ind]:
            merged_arr.append(arr1[arr1_ind])
            arr1_ind += 1
        else:
            merged_arr.append(arr2[arr2_ind])
            arr2_ind += 1

    merged_arr.extend(arr1[arr1_ind:])
    merged_arr.extend(arr2[arr2_ind:])

    return merged_arr


def merge_sort(arr):
    """break array down to the smallest unit and then merge
       sub arrays by value
    """

    if len(arr) <= 1:
        return arr

    mid = floor(len(arr) / 2)

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])


    return merge_lists(left, right)



arr1 = [1, 5, 8, 16, 34]
arr2 = [1, 4, 9, 10, 45, 50]
arr3 = [10, 24, 76, 73, 72, 1, 9]

print(merge_sort(arr3))
