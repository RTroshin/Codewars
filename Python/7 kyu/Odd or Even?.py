def odd_or_even(arr):
    sum = 0

    for n in arr:
        sum += n

    return "odd" if sum % 2 else "even" 
