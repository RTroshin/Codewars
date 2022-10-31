def incrementer(nums):
    return [(num + i) % 10 for num, i in enumerate(nums, 1)]
