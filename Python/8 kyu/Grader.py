def grader(score):
    if score > 0.8 and score < 1:
        return 'A'
    elif score > 0.7 and score < 0.9:
        return 'B'
    elif score > 0.6 and score < 0.8:
        return 'C'
    elif score > 0.5 and score < 0.7:
        return 'D'
    elif score < 0.6 or score > 1:
        return 'F'
