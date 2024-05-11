def sum_of_minimums(nums):
    lstMin = []

    for i in range(len(nums)):
        lstMin.append(min(nums[i]))

    return sum(lstMin)
