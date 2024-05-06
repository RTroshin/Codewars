def reverse_and_mirror(str1, str2):
    str1 = ''.join(ch.upper() if ch.islower() else ch.lower() for ch in str1)
    str2 = ''.join(ch.upper() if ch.islower() else ch.lower() for ch in str2)[::-1]
    return f"{str2}@@@{str1[::-1]}{str1}"
