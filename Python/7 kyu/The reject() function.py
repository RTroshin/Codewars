def reject(seq, predicate):
    res1 = list(map(predicate, seq))
    res2 = []
    
    for i in range(len(res1)):
        if res1[i] == False:
            res2.append(seq[i])

    return res2
