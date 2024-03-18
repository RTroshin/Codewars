def possibly_perfect(key, answers):
    resTrue = [True if key[i] != '_' and key[i] == answers[i] else False for i in range(len(key))]
    resFalse = [False if key[i] != '_' and key[i] != answers[i] else True for i in range(len(key))]

    return True not in resTrue or False not in resFalse
