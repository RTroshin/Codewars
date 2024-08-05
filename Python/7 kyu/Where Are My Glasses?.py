def find_glasses(lst):
    for i, gls in enumerate(lst):
        for j in range(len(gls) - 1):
            if gls[j] == 'O' and gls[j + 1] == '-':
                for n in range(j + 2, len(gls)):
                    if gls[n] == 'O':
                        return i
                    elif gls[n] != '-':
                        break
    return 0
