def how_much_coffee(events):
    coffeeCount = 0

    for i in range(len(events)):
        if events[i].lower() in ["cw", "cat", "dog"]:
            if events[i].isupper():
                coffeeCount += 2
            else:
                coffeeCount += 1

    return coffeeCount
