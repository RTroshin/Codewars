def get_percentage(sent, limit):
    if sent == 0:
        return "No e-mails sent"

    if sent >= limit:
        return "Daily limit is reached"

    if not limit:
        limit = 1000

    res = int(sent / limit * 100)
    res = str(res) + '%'

    return res
