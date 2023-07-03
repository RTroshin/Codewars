def array(str):
    return ' '.join([ch for ch in str.split(',')[1:-1]]) if len(str) > 4 else None
