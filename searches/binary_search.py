from math import floor

def bin_search_exists(arr, target):
    mid = floor(len(arr)/2)

    if len(arr) == 0:
        return False

    if arr[mid] == target:
        return True

    if arr[mid] < target:
        return bin_search_exists(arr[mid + 1:], target)

    if arr[mid] > target:
        return bin_search_exists(arr[:mid],  target)

arr = [1,3,4,5,7,9,12,17,22,25,30]
print(bin_search_exists(arr, 8))


def bin_search_index(arr, target):
    left = 0
    right = len(arr) - 1

    def scan(a, b):
        print("a", a)
        print("b", b)

        if a > b:
            return -1

        mid = floor((a + b)/2)

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            a = mid + 1
            return scan(a, b)

        if arr[mid] > target:
            b = mid - 1
            return scan(a, b)

    return scan(left, right)



arr = [1,3,4,5,7,9,12,17,22,25,30]
print(bin_search_index(arr, 8))

