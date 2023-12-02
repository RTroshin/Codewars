def solution(str):
    return [(str + '_')[i:i + 2] for i in range(0, len(str), 2)]
