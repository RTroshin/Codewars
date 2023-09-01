def camel_case(str):
    return "".join([f"{word[0].upper()}{word[1:]}" for word in str.split()])
