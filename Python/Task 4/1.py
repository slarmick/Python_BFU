def cnt_unq_num(nums):
    set_of_nums = set(nums)
    return len(set_of_nums)

if __name__ == '__main__':
    nums=[int(nums) for nums in input().split()]
    unq_cnt= cnt_unq_num(nums)
    print(f"{unq_cnt}")