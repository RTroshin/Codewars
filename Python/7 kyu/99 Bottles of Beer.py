def sing():
    res = []

    for i in range(97):
        res.append(f"{99 - i} bottles of beer on the wall, {99 - i} bottles of beer.")
        res.append(f"Take one down and pass it around, {98 - i} bottles of beer on the wall.")

    res.append(f"2 bottle of beer on the wall, 2 bottle of beer.")
    res.append(f"Take one down and pass it around, 1 bottle of beer on the wall.")
    res.append(f"1 bottle of beer on the wall, 1 bottle of beer.")
    res.append(f"Take one down and pass it around, no more bottles of beer on the wall.")

    res.append("No more bottles of beer on the wall, no more bottles of beer.")
    res.append("Go to the store and buy some more, 99 bottles of beer on the wall.")

    return res
