def solution(num):
    return sum(i for i in range(num) if not i % 3 or not i % 5)
