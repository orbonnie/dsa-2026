def vanity():
    # define chars map
    key_pad = ["", "", "ABC", "DEF",
            "GHI", "JKL", "MNO",
            "PQRS", "TUV", "WXYZ"]

    # 8945
    number = "+1238578945"
            #     a


    code = "TWIL"

    # define results list
    vanity_numbers = []

    # convert chars to nums
    code_num = ""
    for c in code:
        for i, button in enumerate(key_pad):
            if c in button:
                code_num += str(i)

    print(code_num)

    if code_num in number:
        vanity_numbers.append(number)

    # search nums for match
    # define pointers
    # a = 0
    # b = 1
    # temp_code = ""


    # for n in number:
    #     if a < len(code_num):
    #         print("a", a)
    #         print("n", n)
    #         print("code_num[a]", code_num[a])
    #         if n == code_num[a]:
    #             a += 1

    #         if a == len(code_num) - 1:
    #             vanity_numbers.append(number)


    print(vanity_numbers)

vanity()
