def remove_smallest(numbers):
    return [i for i in numbers if i != min(numbers)] if numbers else []
