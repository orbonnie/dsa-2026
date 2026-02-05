def anagram(s1, s2):
    s1_cnt = {}
    s2_cnt = {}

    if len(s1) != len(s2):
        return False

    for c in s1:
        s1_cnt[c] = s1_cnt.get(c, 0) + 1

    for c in s2:
        s2_cnt[c] = s2_cnt.get(c, 0) + 1

    return s1_cnt == s2_cnt

print(anagram("cinema", "iceman"))
print(anagram("hello", "world"))
