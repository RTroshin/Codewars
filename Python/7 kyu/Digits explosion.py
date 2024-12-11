def explode(str):
    res = ''

    for ch in str:
        res += ch * int(ch)

    return res
