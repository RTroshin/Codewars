def solution(str):
    if len(str) % 2:
        str += '_'
    return [str[i:i + 2] for i in range(0, len(str), 2)]
