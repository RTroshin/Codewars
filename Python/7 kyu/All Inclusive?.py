def contain_all_rots(strng, arr):
    if not strng:
        return False
    if len(strng) < len(arr):
        return False
