def camel_case(str):
    return ''.join([f"{word.capitalize()}" for word in str.split()])
