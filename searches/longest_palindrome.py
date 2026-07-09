import math

def isPalindrome(s: str) -> bool:
    if len(s) < 2: return True
    mid = len(s) // 2
    start = mid - 1
    end = mid if len(s) % 2 == 0 else mid + 1

    # print("preloop", start, end)
    # print("preloop", s[start], s[end])

    while (start >= 0 and end < len(s)):
        # print(start, end)
        # print(s[start], s[end])
        if s[start] == s[end]:
            start -= 1
            end += 1
        else: return False

    return True

def expand(s: str, left: int, right: int):
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            left -= 1
            right += 1
        else:
            break

    return (left + 1, right)

# print(expand("abbcccba", 4, 5))
# oddLeft, oddRight = expand(s, i, i)
# evenLeft, evenRight = expand(s, i, i+1)

# print(expand("abbcccba", 3, 5))
# print(expand("racecar", 2, 4))

# print(isPalindrome("baab"))
# print(isPalindrome("bab"))

def longestPalindrome(s: str) -> str:
    longest = (0, 0)
    if len(s) < 2: return s
    for i, _ in enumerate(s):
        os, oe = expand(s, i, i)
        es, ee = expand(s, i, i+1)

        if (oe - os) > longest[1] - longest[0]:
            longest = (os, oe)
        if (ee - es) > longest[1] - longest[0]:
            longest = (es, ee)

    return s[longest[0] : longest[1]]

print(longestPalindrome("abbcccba"))
