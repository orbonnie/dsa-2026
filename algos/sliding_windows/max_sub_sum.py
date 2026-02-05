def max_sum(nums: list[int], sub: int):
    if len(nums) < sub:
        return
    max_sum = float('-inf')
    end = (-sub) + 1

    for i, n in enumerate(nums[:end]):
        sub_sum = 0
        for j in range(i, i + sub):
            sub_sum += nums[j]

        if sub_sum > max_sum:
            max_sum = sub_sum

    return max_sum


print(max_sum([0, 1, 2, 15, 3, 4, 5, 6, 10, 2, 7, 1], 3))
print(max_sum([0, 1, -2, -15, -3, -4, -5, -6, -10, -2, -7, -1], 4))
print(max_sum([1, 3], 3))
print(max_sum([1, 3, 4], 3))