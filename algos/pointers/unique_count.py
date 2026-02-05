def count_unique(nums):
    if len(nums) == 0:
        return 0

    unique_total = 1
    left = 0
    right = 1
    last_index = len(nums) - 1


    while left < last_index and right <= last_index:
        if nums[left] != nums[right]:
            unique_total += 1
        left += 1
        right = left + 1

    return unique_total


print(count_unique([-3, -3, -2, 0, 1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 10]))
print(count_unique([]))


def count_unique_2(nums):
    if len(nums) == 0:
        return 0

    left = 0
    right = 1


    while left < len(nums) - 1 and right <= len(nums) - 1:
        if nums[left] == nums[right]:
            nums.pop(right)
        else:
            left += 1
            right = left + 1


    return len(nums)


print(count_unique_2([-3, -3, -2, 0, 1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 10]))


def count_unique_set(nums):
    return len(set(nums))

print(count_unique_set([-3, -3, -2, 0, 1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 10]))
