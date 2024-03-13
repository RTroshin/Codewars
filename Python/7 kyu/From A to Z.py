alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def gimme_the_letters(sp):
    sp = sp.split('-')
    return alph[alph.index(sp[0]):alph.index(sp[1]) + 1]
