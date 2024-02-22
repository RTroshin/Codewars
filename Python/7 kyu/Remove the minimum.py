def remove_smallest(nums):
    if nums:
        nums.remove(min(nums))
    return nums
