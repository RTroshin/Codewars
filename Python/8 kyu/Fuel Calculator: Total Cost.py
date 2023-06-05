def fuel_price(litres, price_per_litre):
    discount = 0

    for i in range(litres, 0, -2):
        if discount != 0.25:
            discount += 0.05

    return litres * (price_per_litre - discount)
