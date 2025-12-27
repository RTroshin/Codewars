def sing():
    res = []

    for i in range(101, 1, -1):
        if i > 0 and i < 100:
            res.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            res.append(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.")
        else:
            res.append("No more bottles of beer on the wall, no more bottles of beer.")
            res.append("Go to the store and buy some more, 99 bottles of beer on the wall.")

    return res
