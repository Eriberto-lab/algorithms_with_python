def find_duplicate(nums=None):
    if nums is None or isinstance(nums, str):
        return False

    if len(set(nums)) == len(nums) or isinstance(nums, (int, float)):
        return False

    if any(num < 0 for num in nums):
        return False

    nums_dict = {}
    for num in nums:
        if num in nums_dict:
            return num
        nums_dict[num] = 1

    return False
