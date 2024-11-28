def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    ages_lst = []

    ages_lst.append(age_1 * age_1)
    ages_lst.append(age_2 * age_2)
    ages_lst.append(age_3 * age_3)
    ages_lst.append(age_4 * age_4)
    ages_lst.append(age_5 * age_5)
    ages_lst.append(age_6 * age_6)
    ages_lst.append(age_7 * age_7)
    ages_lst.append(age_8 * age_8)

    ages_lst = sum(ages_lst) ** 0.5

    ages_lst //= 2

    return ages_lst
