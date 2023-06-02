def ensure_question(str):
    return str if len(str) > 1 and str[-1] is '?' else str + '?'
