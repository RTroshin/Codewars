def ensure_question(str):
    return str if len(str) and str[-1] == '?' else f"{str}?"
