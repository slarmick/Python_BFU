def decomp_str(comp_str):
    decomp_str = ""
    i = 0
    while i < len(comp_str):
        if i + 1 < len(comp_str) and comp_str[i + 1].isdigit():
            count = int(comp_str[i + 1])
            decomp_str = decomp_str + comp_str[i] * count
            i += 2
        else:
            decomp_str = decomp_str + comp_str[i]
            i += 1
    return decomp_str


comp_str = input()
decompressed = decomp_str(comp_str)
print(decompressed)
