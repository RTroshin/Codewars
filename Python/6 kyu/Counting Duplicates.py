def duplicate_count(text):
    dupl_let = ""
    text = text.lower()

    for i in text:
        if text.count(i) > 1 and i not in dupl_let:
            dupl_let += i

    return len(dupl_let)
