def starts_with(st, prefix):
    st = st.split()
    return False if not st and prefix else not prefix or st[0] == prefix
