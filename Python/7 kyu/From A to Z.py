alph_low = "abcdefghijklmnopqrstuvwxyz"
alph_high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def gimme_the_letters(sp):
    return alph_low[alph_low.index(sp.split('-')[0]):alph_low.index(sp.split('-')[1]) + 1] if sp[0].islower() else alph_high[alph_high.index(sp.split('-')[0]):alph_high.index(sp.split('-')[1]) + 1]
