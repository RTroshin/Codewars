def catch_sign_change(lst):
    count = 0

    for i in range(len(lst) - 1):
        if lst[i] < 0 and lst[i + 1] < 0:
            count += 0
        elif lst[i] >= 0 and lst[i + 1] >= 0:
            count += 0
        else:
            count += 1

    return count
