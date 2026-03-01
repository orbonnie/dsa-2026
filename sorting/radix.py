from math import floor, pow, log10

def get_column_digit(num, col):
    return floor(abs(num) / pow(10, col)) % 10

def get_col_cnt(n):
    if n == 0: return 1
    return floor(log10(abs(n))) + 1

def get_max_cols(arr):
    max = 0
    for n in arr:
        if get_col_cnt(n) > max:
            max = get_col_cnt(n)

    return max


def radix_sort(arr):
    """Create bucket for 0-9 ints and sorts the numbers into the buckets based on the place value of the number in the 'i' interartion.
       redifines the list in order of the buckets until sorted through all place values.
       Doest not work on neg number out of the box. Must sort neg and pos numbers separately and combine at the end.
    """


    col_count = get_max_cols(arr)

    for i in range(col_count):
        buckets = [[] for _ in range(10)]
        for num in arr:
            bucket = get_column_digit(num, i)
            buckets[bucket].append(num)

        arr = [n for sub in buckets for n in sub]


    return arr


# handles negative values
def radix_sort_neg(arr):
    pos_arr = [n for n in arr if n >= 0]
    neg_arr = [n for n in arr if n < 0]

    pos_col_count = get_max_cols(pos_arr)
    neg_col_count = get_max_cols(neg_arr)

    for i in range(pos_col_count):
        pos_buckets = [[] for _ in range(10)]
        for pos_num in pos_arr:
            pos_bucket = get_column_digit(pos_num, i)
            pos_buckets[pos_bucket].append(pos_num)

        pos_arr = [n for sub in pos_buckets for n in sub]

    for i in range(neg_col_count):
        neg_buckets = [[] for _ in range(10)]
        for neg_num in neg_arr:
            neg_bucket = get_column_digit(neg_num, i)
            neg_buckets[neg_bucket].append(neg_num)

        neg_arr = [n for sub in neg_buckets for n in sub]


    return neg_arr[::-1] + pos_arr


# print(get_max_cols([23, 456, 546027, 43, 5934, 30424]))
# print(get_col_cnt(12345))
# print(get_column_digit(1234, 4))

print(radix_sort_neg([23, 456, -342, 546027, -5, 43, 5934, -8763, 30424, -10]))
print(radix_sort_neg([23, 456, 546027, 43, 5934, 30424]))