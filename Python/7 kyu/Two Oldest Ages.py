def two_oldest_ages(ages):
    ages.sort()

    ages = ages[-2:]

    return ages
