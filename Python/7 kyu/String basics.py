def get_users_ids(st):
    return st.strip().replace("uid", '').replace('#', '').lower().split(", ")
