def solution(str):
    return ''.join([f" {ch}" if ch.isupper() else ch for ch in str])
