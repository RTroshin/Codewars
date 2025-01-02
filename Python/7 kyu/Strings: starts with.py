def starts_with(st, prefix):
    if not st and prefix:
        return False

    st = st.split()

    if not prefix or st[0] == prefix:
        return True
    else:
        return False
