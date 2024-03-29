def possibly_perfect(key, answers):
    return not [True for i, ch in enumerate(key) if ch != '_' and ch == answers[i]] or \
           not [True for i, ch in enumerate(key) if ch != '_' and ch != answers[i]]
