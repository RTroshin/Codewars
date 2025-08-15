def solution(stones):
    RGB = stones[0]
    count = 0

    for i in range(len(stones)):
        if stones[i] not in RGB:
            RGB += stones[i]
        else:
            count += 1
        if len(RGB) == 3:
            RGB = ''

    return count
