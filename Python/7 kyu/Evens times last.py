def even_last(nums):
    res = []
    
    for i in range(len(nums)):
        if not i % 2:
            res.append(nums[i])

    return sum(res) * nums[len(nums) - 1]
