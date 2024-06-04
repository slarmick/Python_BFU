def check_for_include(nums1, nums2):
    nums1_set = set(map(int, nums1.split()))
    nums2_set = set(map(int, nums2.split()))

    if nums1_set.issubset(nums2_set) and nums1_set != nums2_set:
        return True
    else:
        return False


nums1 = input()
nums2 = input()

result = check_for_include(nums1, nums2)
print(result)
