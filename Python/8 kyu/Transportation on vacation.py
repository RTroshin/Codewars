def rental_car_cost(d):
    total = d * 40
    return total if d < 3 else total - 20 if 3 < d < 7 else total - 50
