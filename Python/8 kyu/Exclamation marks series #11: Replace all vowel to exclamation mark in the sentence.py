def replace_exclamation(str):
    return ''.join(['!' if ch in 'aeiouAEIOU' else ch for ch in str])
