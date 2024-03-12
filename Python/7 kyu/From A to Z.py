alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def gimme_the_letters(sp):
    return alph[alph.index(sp.split('-')[0]):alph.index(sp.split('-')[1]) + 1]
