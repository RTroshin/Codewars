def starts_with(st, prefix):
    if not st and prefix:
        return False

    st = st.split()

return not prefix or st[0] == prefix
