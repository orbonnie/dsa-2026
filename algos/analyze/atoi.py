
def myAtoi(s: str) -> int:
    MAX = 2147483647
    MIN = -2147483648
    numStr = ""

    s = s.lstrip()
    if not s or s[0] not in ("+", "-") and not s[0].isnumeric():
        return 0
    else:
        numStr += s[0]

    for c in s[1:]:
        if c.isnumeric():
            numStr += c
            if len(numStr) > 9:
                if int(numStr) > MAX:
                    return MAX
                if int(numStr) < MIN:
                    return MIN
        else:
            break

    return int(numStr) if numStr and numStr not in ("+", "-") else 0

print(myAtoi("  -   123"))
print(myAtoi("  "))
print(myAtoi("+-2"))
print(myAtoi("  +0 123"))
print(myAtoi("2147483647"))
print(myAtoi("2147483648"))
print(myAtoi("-2147483648"))
print(myAtoi("-2147483649"))