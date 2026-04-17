def date_correct(date):
    if not date:
        return date

    date = date.split('.')

    if len(date) != 3:
        return None
    if not date[0].isdecimal() or not date[1].isdecimal() or not date[2].isdecimal():
        return None

    date = '.'.join(date)

    return date
