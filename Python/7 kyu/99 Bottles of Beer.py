def sing():
    res = []

    for i in range(99):
        if 99 - i == 1:
            res.append(f"{99 - i} bottle of beer on the wall, {99 - i} bottle of beer.")
            res.append(f"Take one down and pass it around, no more bottles of beer on the wall.")
        else:
            res.append(f"{99 - i} bottles of beer on the wall, {99 - i} bottles of beer.")

            if 98 - i == 1:
                res.append(f"Take one down and pass it around, {98 - i} bottle of beer on the wall.")
            else:
                res.append(f"Take one down and pass it around, {98 - i} bottles of beer on the wall.")

    res.append("No more bottles of beer on the wall, no more bottles of beer.")
    res.append("Go to the store and buy some more, 99 bottles of beer on the wall.")

    return res
