def ensure_question(str):
    return str if str and str[-1] == '?' else f"{str}?"
