def correct_polish_letters(str): 
    polish_alph = {'ą': 'a',
                   'ć': 'c',
                   'ę': 'e',
                   'ł': 'l',
                   'ń': 'n',
                   'ó': 'o',
                   'ś': 's',
                   'ź': 'z'}

    return ''.join(polish_alph[ch] if ch in "ąćęłńóśź" else ch for ch in str)
