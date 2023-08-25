def ensure_question(str):
    return str if len(str) and str[-1] is '?' else str + '?'
