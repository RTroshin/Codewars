def how_much_coffee(events):
    coffeeCount = 0

    for event in events:
        if event.lower() in ["cw", "cat", "dog"]:
            if event.isupper():
                coffeeCount += 2
            else:
                coffeeCount += 1

    return coffeeCount
