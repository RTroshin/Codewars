def final_grade(exam, projects):
    if 50 <= exam < 75 and 2 <= projects < 5:
        return 75
    elif 75 <= exam <= 90 and 5 <= projects <= 10:
        return 90
    elif exam > 90 and projects > 10:
        return 100
    else:
        return 0
