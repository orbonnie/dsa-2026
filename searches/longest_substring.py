def lengthOfLongestSubstring(s: str) -> int:
    found = ""
    longest = 0

    for i,c in enumerate(s):
        if c not in found:
            found += c
            if len(found) > longest:
                longest = len(found)
        else:
            start = found.find(c)
            print("start", start)
            found = found[start + 1:]  + c
            print("found", found)


    return longest


print(lengthOfLongestSubstring("aab"))

print(lengthOfLongestSubstring("dvdf"))
