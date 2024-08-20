def solve(s):
    count1, count2, count3, count4 = 0, 0, 0, 0

    for ch in s:
        if ch.isupper():
            count1 += 1
        elif ch.islower():
            count2 += 1
        elif ch.isdigit():
            count3 += 1
        else:
            count4 += 1

    return [count1, count2, count3, count4]
