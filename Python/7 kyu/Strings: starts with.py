def starts_with(st, prefix):
    if not prefix:
        return True
    elif not st:
        return False

    st = st.split()

    if st[0] == prefix:
        return True
    else:
        return False
