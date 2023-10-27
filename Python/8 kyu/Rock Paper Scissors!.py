def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif len(p1) * 2 == len(p2):
        return "Player 1 won!"
    elif len(p2) * 2 == len(p1):
        return "Player 2 won!"
    elif len(p1) > len(p2):
        return "Player 1 won!"
    else:
        return "Player 2 won!"
