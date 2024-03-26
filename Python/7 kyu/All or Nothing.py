def possibly_perfect(key, answers):
    return True not in [True for i in range(len(key)) if key[i] != '_' and key[i] == answers[i]] or \
           True not in [True for i in range(len(key)) if key[i] != '_' and key[i] != answers[i]]
