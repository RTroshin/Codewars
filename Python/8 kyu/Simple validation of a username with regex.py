def validate_usr(username):
    for ch in username:
        if not ch.isalpha() and not ch.isdigit() and not ch == '_':
            return False

    return username == username.lower() and 3 < len(username) < 17
