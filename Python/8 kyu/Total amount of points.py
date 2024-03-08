def points(games):
    return sum(3 if score[0] > score[-1] else 1 if score[0] == score[-1] else 0 for score in games)
