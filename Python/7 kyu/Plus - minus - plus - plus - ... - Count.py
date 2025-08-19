def catch_sign_change(lst):
    count = 0

    for i in range(len(lst) - 1):
        if not (lst[i] < 0 and lst[i + 1] < 0 or lst[i] >= 0 and lst[i + 1] >= 0):
            count += 1

    return count
