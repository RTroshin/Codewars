def reject(seq, predicate):
    res1 = map(predicate, seq)
    res1 = list(res1)
    res2 = []
    
    for i in range(len(res1)):
        if res1[i] == False:
            res2.append(seq[i])

    return res2
