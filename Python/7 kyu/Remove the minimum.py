def remove_smallest(nums):
    i = nums.index(min(nums)) if nums else 0
    return nums[:i] + nums[i + 1:]
