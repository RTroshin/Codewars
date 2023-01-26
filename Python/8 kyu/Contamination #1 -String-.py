def contamination(text, char):
    return "".join([char if text and char else "" for i in range(len(text))])
