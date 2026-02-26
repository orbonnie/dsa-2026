def naiveSearch(long: str, short: str):
    found_index = 0
    found_word = ""
    found_count = 0

    # iterate over the long string
    for i, c in enumerate(long):
        # check for the first letter in the short string
            if c == short[found_index]:
                # once first letter is found check for the next letter in the short string
                if found_index == len(short) - 1:
                    found_count += 1
                    found_index = 0
                else:
                    found_index += 1
            else:

                found_index = 0

    return found_count



# print(naiveSearch("submarine maritime mar", "mar"))
print(naiveSearch("lola loled loudly lol loalo", "lol"))
