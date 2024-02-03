def high_and_low(nums):
    nums = sorted(list(map(int, nums.split())))
    return f"{nums[-1]} {nums[0]}"
