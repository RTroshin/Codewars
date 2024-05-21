def get_users_ids(st):
    return [ID[3:] for ID in st.strip().replace('#', '').lower().split(", ")]
