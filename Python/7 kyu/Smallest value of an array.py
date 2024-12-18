def find_smallest(nums, to_return):
    if to_return == "value":
        return min(nums)
    elif to_return == "index":
        return nums.index(min(nums))
