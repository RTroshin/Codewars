def possibly_perfect(key, answers):
    return not [True for i in range(len(key)) if key[i] != '_' and key[i] == answers[i]] or \
           not [True for i in range(len(key)) if key[i] != '_' and key[i] != answers[i]]
