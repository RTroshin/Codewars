def even_last(nums):
    if not nums:
        return 0

    res = []

    for i in range(len(nums)):
        if not i % 2:
            res.append(nums[i])
    
    return sum(res) * nums[len(nums) - 1]
