def anagram(s1, s2):
    s1_cnt = {}

    if len(s1) != len(s2):
        return False

    for c in s1:
        s1_cnt[c] = s1_cnt.get(c, 0) + 1

    for c in s2:
        if c in s1_cnt:
            s1_cnt[c] -= 1
            if s1_cnt[c] == 0:
                del s1_cnt[c]
        else:
            return False

    return s1_cnt == {}

print(anagram("cinema", "iceman"))
print(anagram("hello", "world"))
