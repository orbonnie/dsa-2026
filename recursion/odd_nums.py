def get_odd_nums(arr, odds = []):
    end_index = len(arr) -1
    if len(arr) == 0:
        return odds

    if arr[end_index] % 2 == 1:
        odds.append(arr[end_index])
    arr.pop(end_index)

    return get_odd_nums(arr, odds)


print(get_odd_nums([1,4,5,3,6,8,9]))


def get_odds_build(arr):
    odds = []
    length = len(arr)

    if length == 0:
        return odds

    if arr[length - 1] % 2 == 1:
        odds.append(arr[length - 1])

    arr.pop(length - 1)

    odds += get_odds_build(arr)

    return odds

print(get_odds_build([1,4,5,3,6,8,9]))


def get_odds_helper(arr):
    odds = []

    def sort_nums(helper_arr):
        length = len(helper_arr)
        if length == 0:
            return

        if helper_arr[length - 1] % 2 == 1:
            odds.append(helper_arr[length -1])

        helper_arr.pop(length - 1)

        sort_nums(helper_arr)

    sort_nums(arr)
    return odds

print(get_odds_helper([1,4,5,3,6,8,9]))