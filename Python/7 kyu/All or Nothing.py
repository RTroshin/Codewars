def possibly_perfect(key, answers):
    resTrue = [True for i in range(len(key)) if key[i] != '_' and key[i] == answers[i]]
    resFalse = [False for i in range(len(key)) if key[i] != '_' and key[i] != answers[i]]

    return True not in resTrue or False not in resFalse
