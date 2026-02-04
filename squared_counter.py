def same(base, squared):
    based_cnt = {}
    sq_cnt = {}

    if len(base) != len(squared):
        return False

    for b in base:
        if b in based_cnt:
            based_cnt[b] += 1
        else:
            based_cnt[b] = 1

    for s in squared:
        if s in sq_cnt:
            sq_cnt[s] += 1
        else:
            sq_cnt[s] = 1

    for key in based_cnt:
        if key ** 2 not in sq_cnt or sq_cnt[key ** 2] != based_cnt[key]:
            return False

    return True


print(same([1, 3, 2, 2, 5], [1, 4, 4, 9, 36]))
