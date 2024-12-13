def explode(str):
    return ''.join(ch * int(ch) for ch in str)
