def format_money(amount):
    return '$' + str(amount) if len(str(amount)) > 4 else str(amount) + '0'
