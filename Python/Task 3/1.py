def comp_string(s):
    comp_str = ""
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            if count > 1:
                comp_str = comp_str + s[i] + str(count)
            else:
                comp_str = comp_str + s[i]
            count = 1
    if count > 1:
        comp_str = comp_str + s[-1] + str(count)
    else:
        comp_str = comp_str + s[-1]
    return comp_str


input_str = input()
compressed = comp_string(input_str)
print(compressed)
