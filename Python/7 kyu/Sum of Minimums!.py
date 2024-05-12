def sum_of_minimums(nums):
    return sum([min(nums[i]) for i in range(len(nums))])
