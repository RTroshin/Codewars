def possibly_perfect(key, answers):
    resTrue = []
    resFalse = []

    for i in range(len(key)):
        if key[i] != '_':
            resTrue.append(True) if key[i] == answers[i] else resTrue.append(False)

    for i in range(len(key)):
        if key[i] != '_':
            resFalse.append(False) if key[i] != answers[i] else resFalse.append(True)

    return True not in resTrue or False not in resFalse
