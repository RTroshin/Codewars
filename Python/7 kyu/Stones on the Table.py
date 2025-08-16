def solution(stones):
    RGB = stones[0]
    count = 0

    for stone in stones:
        if stone not in RGB:
            RGB += stone
        else:
            count += 1
        if len(RGB) == 3:
            RGB = ''

    return count
