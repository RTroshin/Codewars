alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def gimme_the_letters(sp):
    return alph[alph.index(sp[0]):alph.index(sp[2]) + 1]
