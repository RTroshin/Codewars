def get_percentage(sent, limit):
    if sent == 0:
        return "No e-mails sent"
    elif sent >= limit:
        return "Daily limit is reached"
    elif not limit:
        limit = 1000

    res = int(sent / limit * 100)

    return str(res) + '%'
