def count_smileys(arr):
    count = 0

    for face in arr:
        if len(face) == 2 and face[0] in ":;" and face[-1] in ")D":
            count += 1
        elif len(face) == 3 and face[0] in ":;" and face[1] in "-~" and face[-1] in ")D":
            count += 1

    return count
