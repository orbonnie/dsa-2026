def sum_zero(nums):
    start = 0
    end = 1
    result = []
    last_index = len(nums) - 1

    while start < end and end <= last_index:
        if nums[start] + nums[end] == 0:
            result.append((nums[start], nums[end]))
            print("if", nums[start], nums[end], last_index)
            return result
        elif start < last_index and end < last_index:
            print("first elif", nums[start], nums[end], last_index)
            end += 1
        elif start < last_index and end == last_index:
            print("second elif", nums[start], nums[end], last_index)
            start += 1
            end = start + 1

    return result


print(sum_zero([-4, -3, -2, -1, 0, 1, 5, 10]))
