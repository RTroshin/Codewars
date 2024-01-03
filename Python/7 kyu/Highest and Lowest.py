def high_and_low(nums):
    nums = sorted(list(map(int, nums.split(' '))))
    return str(nums[-1]) + ' ' + str(nums[0])
