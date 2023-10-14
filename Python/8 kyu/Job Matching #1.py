def match(candidate, job):
    return candidate["min_salary"] <= job["max_salary"] + candidate["min_salary"] / 10
