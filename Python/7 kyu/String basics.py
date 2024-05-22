def get_users_ids(str):
    return [ID[3:] for ID in str.strip().replace('#', '').lower().split(", ")]
