def count_str_occurr(strings):
    occurrs = {}

    for string in strings:
        if string in occurrs:
            occurrs[string] += 1
        else:
            occurrs[string] = 1

    unq_strs = list(occurrs.keys())
    res = [str(occurrs[string]) for string in unq_strs]
    print(' '.join(res))


input_strs = input()
strs = input_strs.split(', ')

count_str_occurr(strs)
