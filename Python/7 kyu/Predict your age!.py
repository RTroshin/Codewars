def predict_age(*ages):
    ages_lst = []

    for age in ages:
        ages_lst.append(age * age)

    return (sum(ages_lst) ** 0.5) // 2
