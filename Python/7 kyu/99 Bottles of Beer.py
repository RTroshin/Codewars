def sing():
    res = []

    for i in range(101, 1, -1):
        if i - 1 == 1:
            res.append(f"{i - 1} bottle of beer on the wall, {i - 1} bottle of beer.")
            res.append(f"Take one down and pass it around, {i - 2} bottle of beer on the wall.")
        elif i - 2 == 1:
            res.append(f"{i - 1} bottles of beer on the wall, {i - 1} bottles of beer.")
            res.append(f"Take one down and pass it around, {i - 2} bottle of beer on the wall.")
        elif i > 0 and i < 101:
            res.append(f"{i - 1} bottles of beer on the wall, {i - 1} bottles of beer.")
            res.append(f"Take one down and pass it around, {i - 2} bottles of beer on the wall.")

    res.append("No more bottles of beer on the wall, no more bottles of beer.")
    res.append("Go to the store and buy some more, 99 bottles of beer on the wall.")

    return res
