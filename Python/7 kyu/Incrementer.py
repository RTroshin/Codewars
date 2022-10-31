def incrementer(nums):
    return [num + i + 1 if num + i + 1 < 10 else (num + i + 1) % 10 for num, i in enumerate(nums)]
