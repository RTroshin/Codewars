ingredients = {'t': "tomato",
               'l': "lettuce",
               'c': "cheese",
               'g': "guacamole",
               's': "salsa"}

def tacofy(word):
    return f"shell {' '.join('beef' if ch in 'aeiou' else ingredients.get(ch, '') for ch in word.lower())} shell".split()
