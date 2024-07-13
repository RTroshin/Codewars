lojban_dict = {1: "pa", 4: "vo", 7: "ze",
               2: "re", 5: "mu", 8: "bi",
               0: "no", 3: "ci", 6: "xa",
               9: "so"}

def convert_lojban(lojban):
    return ''.join(lojban_dict.get(int(i)) for i in str(lojban))
