def possibly_perfect(key, answers):
    resTrue = []
    resFalse = []

    for i in range(len(key)):
        if key[i] != '_':
            if key[i] == answers[i]:
                resTrue.append(True)
            else:
                resTrue.append(False)

    for i in range(len(key)):
        if key[i] != '_':
            if key[i] != answers[i]:
                resFalse.append(False)
            else:
                resFalse.append(True)

    return True if True not in resTrue or False not in resFalse else False
