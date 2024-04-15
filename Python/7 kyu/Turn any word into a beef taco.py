ingredients = {'a': "beef", 'e': "beef",  'i': "beef", 'o': "beef", 'u': "beef", 't': "tomato", 'l': "lettuce", 'c': "cheese", 'g': "guacamole", 's': "salsa"}

def tacofy(word):
    return ["shell"] + [ingredients.get(ch.lower()) for ch in word if ch.lower() in "aeioutlcgs"] + ["shell"]
