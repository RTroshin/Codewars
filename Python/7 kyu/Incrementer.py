def incrementer(nums):
    return [nums[i] + i + 1 if nums[i] + i + 1 < 10 else (nums[i] + i + 1) % 10 for i in range(len(nums))]
