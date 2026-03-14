def how_much_coffee(events):
    coffeeCount = 0

    for event in events:
        if event.lower() in ["cw", "cat", "dog"]:
            coffeeCount += 2 if event.isupper() else 1

    return "You need extra sleep" if coffeeCount > 3 else coffeeCount
