def solution(nums):
    if not nums:
        return []

    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums
