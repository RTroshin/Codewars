def validate_hello(greetings):
    for word in ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]:
        if word in greetings.lower():
            return True
    return False
